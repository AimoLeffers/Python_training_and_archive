import logging
import tkinter as tk
from tkinter.filedialog import askopenfilename


class __FilePickWindow:
    """Wrapper class for a simple fileselection gui"""

    def __init__(self, windowtitle, filetypes, initial_dir):
        """Initial setup of all variables"""
        self.windowtitle = windowtitle
        self.filetypes = filetypes
        self.initial_dir = initial_dir
        self.window = None
        self.selected_path = None
        return

    def show(self):
        """Creates the gui, shows it to the user and may retrive the filepath of a selected file"""
        self.selected_path = None
        self.window = tk.Tk()
        self.window.withdraw()
        self.selected_path = askopenfilename(title=self.windowtitle,
                                             filetypes=self.filetypes,
                                             initialdir=self.initial_dir)
        return


def __main():
    logging.basicConfig(level=logging.INFO)
    print(get_filepath_from_user("Test", [("all", "*")]))


def get_filepath_from_user(windowtitle: str, filetypes: list, initial_directory='/'):
    """
    Returns a filepath, which can be choosen by the user via gui.

    :param windowtitle: Defines the name of the window.
    :param filetypes: A list of tuples which defines the names and fileendings of files, which can be selected.
    :param initial_directory: Path of the initialy opend folder.
    :return: filepath: Path of the file, selected by the user. Returns False if no file was choosen.
    """
    logger = logging.getLogger("get_filepath_from_user")
    logger.log(logging.INFO, "get_filepath_from_user() is called")

    if not isinstance(windowtitle, str):
        logger.log(logging.ERROR, f"{str(type(windowtitle))} instead of str was passed as windowtitle")
        raise TypeError("Argument 'windowtitle' was not a String")

    if not isinstance(filetypes, list):
        logger.log(logging.ERROR, f"{str(type(filetypes))} instead of a list was passed as filetypes")
        raise TypeError("Argument 'filetypes' was not a List")

    if not isinstance(initial_directory, str):
        logger.log(logging.ERROR, f"{str(type(initial_directory))} instead of str was passed as initial_directory")
        raise TypeError("Argument 'initial_directory' was not a String")

    fpw = __FilePickWindow(windowtitle, filetypes, initial_directory)
    fpw.show()
    filepath = fpw.selected_path

    if filepath == "":
        logger.log(logging.WARNING, "No file was picked")
        filepath = False

    return filepath


if __name__ == "__main__":
    __main()
