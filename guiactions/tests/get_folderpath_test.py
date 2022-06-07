import unittest
from guiactions.get_folderpath import get_folderpath_from_user


class TestGetFolderpath(unittest.TestCase):
    def test_wrong_argument_types(self):
        self.assertRaises(TypeError, get_folderpath_from_user, 1, )
        self.assertRaises(TypeError, get_folderpath_from_user, "Title", 1)


if __name__ == '__main__':
    unittest.main()
