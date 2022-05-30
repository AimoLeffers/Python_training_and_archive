import unittest
from guiactions.get_filepath import get_filepath_from_user


class TestGetFilepath(unittest.TestCase):
    def test_wrong_argument_types(self):
        self.assertRaises(TypeError, get_filepath_from_user, 1, [("Textfiles", "*.txt"), ("Images", "*.jpg")])
        self.assertRaises(TypeError, get_filepath_from_user, "Title", 1)
        self.assertRaises(TypeError, get_filepath_from_user, "Title", [("Textfiles", "*.txt"), ("Images", "*.jpg")], 1)


if __name__ == '__main__':
    unittest.main()
