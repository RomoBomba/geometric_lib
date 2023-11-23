import unittest

def area(a, b): 
    return a * b 

def perimeter(a, b): 
    return (a + b) * 2

class RectangleTests(unittest.TestCase):
    def test_area(self):
        '''
        Тестирование функции площади при вводе положительных чисел
        '''
        self.assertEqual(area(5, 4), 20)
        '''
        Тестирование функции площади при вводе числа с плавающей точкой
        '''
        self.assertEqual(area(5.3, 2), 10.6)
        '''
        Тестирование функции площади при вводе 0
        '''
        self.assertEqual(area(0, 5), 0)
        '''
        Тестирование функции площади при вводе отрицательных чисел
        '''
        self.assertEqual(area(-6, -6), "Error")

    def test_perimeter(self):
        '''
        Тестирование функции периметра при вводе положительных чисел
        '''
        self.assertEqual(perimeter(3, 4), 14)
        '''
        Тестирование функции периметра при вводе числа с плавающей точкой
        '''
        self.assertEqual(perimeter(5.3, 2), 14.6)
        '''
        Тестирование функции периметра при вводе 0
        '''
        self.assertEqual(perimeter(0, 8), 16)
        '''
        Тестирование функции периметра при вводе отрицательных чисел
        '''
        self.assertEqual(perimeter(-7, 9), "Error")


if __name__ == '__main__':
    unittest.main()
