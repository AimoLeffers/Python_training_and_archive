import unittest
from configuration_files.configuration import Configuration


class TestConfiguration(unittest.TestCase):
    def test_init_with_empty_path(self):
        self.assertRaises(FileNotFoundError, Configuration, "")

    def test_init_without_existing_config_file(self):
        test_config = Configuration("new_test_config.testconf")
        self.assertEqual(test_config.sections, [])
        test_config.remove_config_file()

    def test_init_with_existing_config_file(self):
        test_config = Configuration("empty_test_config.testconf")
        self.assertEqual(test_config.sections, [])

    def test_read_write_operation(self):
        section_name = "DEFAULT"
        test_config = Configuration("test_config.testconf")
        test_config.content[section_name] = {"test_1_key": "test_1_value",
                                             "test_2_key": "test_2_value"}
        test_config.save_to_file()
        test_config.content[section_name]["test_1_key"] = ""
        test_config.content[section_name]["test_2_key"] = ""
        test_config.read_from_file()
        self.assertEqual(test_config.content[section_name]["test_1_key"], "test_1_value")
        self.assertEqual(test_config.content[section_name]["test_2_key"], "test_2_value")
        test_config.remove_config_file()

    def test_add_key_to_existing_config_file(self):
        section_name = "DEFAULT"
        test_config = Configuration("test_config.testconf")
        # Create config file
        test_config.content[section_name] = {"test_1_key": "test_1_value",
                                             "test_2_key": "test_2_value"}
        test_config.save_to_file()
        test_config.content[section_name]["test_1_key"] = ""
        test_config.content[section_name]["test_2_key"] = ""
        test_config.read_from_file()
        self.assertEqual(test_config.content[section_name]["test_1_key"], "test_1_value")
        self.assertEqual(test_config.content[section_name]["test_2_key"], "test_2_value")

        # Add additional key-value pair for the config file
        test_config.content[section_name]["test_3_key"] = "test_3_value"
        test_config.save_to_file()

        # Reset the config within the memory and check if in the file are the correct values
        test_config.content[section_name]["test_1_key"] = ""
        test_config.content[section_name]["test_2_key"] = ""
        test_config.content[section_name]["test_3_key"] = ""

        test_config.read_from_file()
        self.assertEqual(test_config.content[section_name]["test_1_key"], "test_1_value")
        self.assertEqual(test_config.content[section_name]["test_2_key"], "test_2_value")
        self.assertEqual(test_config.content[section_name]["test_3_key"], "test_3_value")

        test_config.remove_config_file()

    def test_with_removed_config_file(self):
        test_config = Configuration("test_config.test_conf")
        test_config.remove_config_file()
        self.assertRaises(FileNotFoundError, test_config.remove_config_file)
        self.assertRaises(FileNotFoundError, test_config.read_from_file)
        self.assertRaises(FileNotFoundError, test_config.save_to_file)
