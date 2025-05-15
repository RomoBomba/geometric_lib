import os
import sys
import errno
import subprocess
from llfuse import Operations, FUSEError
from llfuse import init as fuse_init, main as fuse_main

class ConverterFS(Operations):
    def __init__(self, root):
        self.root = os.path.realpath(root)
        self.inode_count = 1
        self.path_to_inode = {'/': 1}  # Корневой inode

    def _get_path(self, inode):
        for path, idx in self.path_to_inode.items():
            if idx == inode:
                return os.path.join(self.root, path.lstrip('/'))
        raise FUSEError(errno.ENOENT)

    def getattr(self, inode, ctx):
        path = self._get_path(inode)
        try:
            st = os.lstat(path)
            return {
                'st_mode': st.st_mode,
                'st_size': st.st_size,
                'st_atime': st.st_atime,
                'st_mtime': st.st_mtime,
                'st_uid': os.getuid(),
                'st_gid': os.getgid()
            }
        except FileNotFoundError:
            raise FUSEError(errno.ENOENT)

    def lookup(self, parent_inode, name, ctx):
        parent_path = self._get_path(parent_inode)
        path = os.path.join(parent_path, name)
        if not os.path.exists(path):
            raise FUSEError(errno.ENOENT)
        return os.stat(path).st_ino

    def readdir(self, inode, offset):
        path = self._get_path(inode)
        entries = [('.', inode), ('..', inode)]
        
        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)
            entries.append((entry, os.stat(entry_path).st_ino))
            if entry.endswith('.png'):
                jpg_entry = entry.replace('.png', '.jpg')
                entries.append((jpg_entry, 0))  # Inode 0 для виртуальных файлов
        return entries

    def open(self, inode, flags, ctx):
        path = self._get_path(inode)
        if path.endswith('.jpg'):
            png_path = path.replace('.jpg', '.png')
            if os.path.exists(png_path):
                subprocess.run(['convert', png_path, path], check=True)
        return os.open(path, flags)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <source_dir> <mount_dir>")
        sys.exit(1)

    # Исправленные опции монтирования
    mount_options = {
        'allow_other': True,
        'fsname': 'converterfs',
        'subtype': 'fuse_converter'
    }

    try:
        fuse_init(ConverterFS(sys.argv[1]), sys.argv[2], mount_options)
        fuse_main()
    except KeyboardInterrupt:
        pass
    finally:
        from llfuse import close as fuse_close
        fuse_close()
