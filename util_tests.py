import unittest
import util_class

stringInput = util_class.utils('hello')
floatInput = util_class.utils(123.45)
intInput = util_class.utils(12345)


class MyTestCase(unittest.TestCase):
    def test_reversed(self):
        self.assertRaises(TypeError, lambda: stringInput.reversed())
        self.assertRaises(TypeError, lambda: floatInput.reversed())
        self.assertRaises(TypeError, intInput.reversed())
        self.assertRaises(TypeError, lambda: stringInput.formatter())
        self.assertRaises(TypeError, lambda: floatInput.formatter())
        self.assertRaises(TypeError, intInput.formatter())


if __name__ == '__main__':
    unittest.main()
