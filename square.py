import unittest

def area(a):
    return a * a


def perimeter(a):
    return 4 * a

class SquareTest(unittest.TestCase):
    def test_area(self):
        '''
        Тестирование функции площади при вводе положительных чисел
        '''
        self.assertEqual(area(6), 36)
        '''
        Тестирование функции площади при вводе числа с плавающей точкой
        '''
        self.assertAlmostEqual(area(6.9), 47.61, places=2)
        '''
        Тестирование функции площади при вводе 0
        '''
        self.assertEqual(area(0), 0)
        '''
        Тестирование функции площади при вводе отрицательных чисел
        '''
        self.assertEqual(area(-7), "Error")

    def test_perimeter(self):
        '''
        Тестирование функции периметра при вводе положительных чисел
        '''
        self.assertEqual(perimeter(4), 16)
        '''
        Тестирование функции периметра при вводе числа с плавающей точкой
        '''
        self.assertEqual(perimeter(2.3), 9.2)
        '''
        Тестирование функции периметра при вводе 0
        '''
        self.assertEqual(perimeter(0), 0)
        '''
        Тестирование функции периметра при вводе отрицательных чисел
        '''
        self.assertEqual(perimeter(-5), "Error")


if __name__ == '__main__':
    unittest.main()
