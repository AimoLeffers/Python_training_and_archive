import configparser
import os


class Configuration:
    """
    This class handles the communication with an external configfile and is based on the module "configparser"
    """
    def __init__(self, path: str):
        """
        On class initialisation it will be checked if under the provided path a configfile can be found.
        If there is a configfile, the contents will be red. Otherwise, a new and empty config file will be created.

        self.path:      full filepath (with filename) to the config file
        self.sections:  List of sections within the configfile
        self.content:   configparser object (see: https://docs.python.org/3/library/configparser.html)

        """
        if path == "":  # Error checks
            raise FileNotFoundError(f"Invalid path provided ({path})")

        self.path = path
        self.content = configparser.ConfigParser()
        self.sections = []

        if os.path.isfile(self.path):
            # Read config, if a configfile is present
            self.content.read(self.path)
            self.sections = self.content.sections()
        else:
            self.path = path
            with open(path, 'w') as configfile:
                self.content.write(configfile)

    def save_to_file(self):
        """
        Writes the current config contents to the defined configfile.
        """
        if os.path.isfile(self.path):
            with open(self.path, 'w') as configfile:
                self.content.write(configfile)
        else:
            raise FileNotFoundError(f"configfile not found! ({self.path})")

    def read_from_file(self):
        """
        Reads the configuration from the defined config file. The current config content will be overwritten.
        """
        if os.path.isfile(self.path):
            self.content.read(self.path)
        else:
            raise FileNotFoundError(f"configfile not found! ({self.path})")

    def remove_config_file(self):
        if os.path.isfile(self.path):
            os.remove(self.path)
        else:
            raise FileNotFoundError(f"configfile not found! ({self.path})")
