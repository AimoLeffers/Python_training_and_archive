import myfunctions
import unittest


class TestMultiply(unittest.TestCase):

    def test_with_two_positive(self):
        self.assertEqual(myfunctions.multiply_with_loop_imperfect(17, 19), 17 * 19)
        self.assertEqual(myfunctions.multiply_with_loop_imperfect(123424, 131569), 123424 * 131569)
        self.assertEqual(myfunctions.multiply_with_loop_imperfect(1, 2), 1 * 2)

    def test_with_one_zero(self):
        self.assertEqual(myfunctions.multiply_with_loop_imperfect(17, 0), 0)
        self.assertEqual(myfunctions.multiply_with_loop_imperfect(0, 17), 0)

    def test_with_two_zeros(self):
        self.assertEqual(myfunctions.multiply_with_loop_imperfect(0, 0), 0)

    def test_with_one_negative(self):
        self.assertEqual(myfunctions.multiply_with_loop_imperfect(17, - 19), 17 * (-19))
        self.assertEqual(myfunctions.multiply_with_loop_imperfect(-19, 17), (-19) * 17)

    def test_with_two_negative(self):
        self.assertEqual(myfunctions.multiply_with_loop_imperfect(-17, -19), (-17) * (-19))


class TestMultiplyBetter(unittest.TestCase):

    def test_with_two_positive(self):
        self.assertEqual(myfunctions.multiply_with_loop_better(17, 19), 17 * 19)
        self.assertEqual(myfunctions.multiply_with_loop_better(123424, 131569), 123424 * 131569)
        self.assertEqual(myfunctions.multiply_with_loop_better(1, 2), 1 * 2)

    def test_with_one_zero(self):
        self.assertEqual(myfunctions.multiply_with_loop_better(17, 0), 0)
        self.assertEqual(myfunctions.multiply_with_loop_better(0, 17), 0)

    def test_with_two_zeros(self):
        self.assertEqual(myfunctions.multiply_with_loop_better(0, 0), 0)

    def test_with_one_negative(self):
        self.assertEqual(myfunctions.multiply_with_loop_better(17, - 19), 17 * (-19))
        self.assertEqual(myfunctions.multiply_with_loop_better(-19, 17), (-19) * 17)

    def test_with_two_negative(self):
        self.assertEqual(myfunctions.multiply_with_loop_better(-17, -19), (-17) * (-19))


class TestIntegerLength(unittest.TestCase):

    def test_with_positive_integer(self):
        self.assertEqual(myfunctions.length_of_integer(123456), 6)
        self.assertEqual(myfunctions.length_of_integer(1), 1)
        self.assertEqual(myfunctions.length_of_integer(10), 2)

    def test_with_negative_integer(self):
        self.assertEqual(myfunctions.length_of_integer(-123), 4)
        self.assertEqual(myfunctions.length_of_integer(-1), 2)
        self.assertEqual(myfunctions.length_of_integer(-123456), 7)

    def test_with_zero(self):
        self.assertEqual(myfunctions.length_of_integer(0), 1)

    def test_with_invalid_type(self):
        self.assertRaises(TypeError, myfunctions.length_of_integer, "12345")
        self.assertRaises(TypeError, myfunctions.length_of_integer, "Hello")
        self.assertRaises(TypeError, myfunctions.length_of_integer, True)
        self.assertRaises(TypeError, myfunctions.length_of_integer, 123.456)
        self.assertRaises(TypeError, myfunctions.length_of_integer, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
