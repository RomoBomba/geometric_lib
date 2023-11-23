import unittest

def area(a, h): 
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c 


class TriangleTest(unittest.TestCase):
    def test_area(self):
        '''
        Тестирование функции площади при вводе 0
        '''
        self.assertEqual(area(0, 10), 0)
        '''
        Тестирование функции площади при вводе числа с плавающей точкой
        '''
        self.assertAlmostEqual(area(3.5, 6), 10.5, places=2)
        '''
        Тестирование функции площади при вводе отрицательных чисел
        '''
        self.assertEqual(area(-5, 7), "Error")
        '''
        Тестирование функции площади при вводе положительных чисел
        '''
        self.assertEqual(area(4, 8), 16)


    def test_perimeter(self):
        '''
        Тестирование функции периметра при вводе 0
        '''
        self.assertEqual(perimeter(0, 0, 0), 0)
        '''
        Тестирование функции периметра при вводе числа с плавающей точкой
        '''
        self.assertAlmostEqual(perimeter(2.5, 3, 4.5), 10, places=2)
        '''
        Тестирование функции периметра при вводе отрицательных чисел
        '''
        self.assertEqual(perimeter(-2, -3, -4), "Error")
        '''
        Тестирование функции периметра при вводе положительных чисел
        '''
        self.assertEqual(perimeter(3, 4, 5), 12)

if __name__ == '__main__':
    unittest.main()
