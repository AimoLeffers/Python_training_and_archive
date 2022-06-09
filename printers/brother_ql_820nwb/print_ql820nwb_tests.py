import unittest
from printers.brother_ql_820nwb.print_ql820nwb import mm_to_dots
from printers.brother_ql_820nwb.print_ql820nwb import dots_to_hex


class MmToDotsTests(unittest.TestCase):
    def test_positve_floats(self):
        self.assertEqual(mm_to_dots(50.8), 600)
        self.assertEqual(mm_to_dots(25.4), 300)
        self.assertEqual(mm_to_dots(10.0), 118)
        self.assertEqual(mm_to_dots(1.0), 12)

    def test_positive_ints(self):
        self.assertRaises(ValueError, mm_to_dots, 2)

    def test_negative_values(self):
        self.assertRaises(ValueError, mm_to_dots, -50.8)


class DotsToHexTests(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(dots_to_hex(600), (b"\x58", b"\x02"))
        self.assertEqual(dots_to_hex(50), (b"\x32", b"\x00"))
        self.assertEqual(dots_to_hex(8000), (b"\x40", b"\x1F"))
        self.assertRaises(ValueError, dots_to_hex, 8001)

    def test_negative_values(self):
        self.assertRaises(ValueError, dots_to_hex, -5)


if __name__ == '__main__':
    unittest.main()
