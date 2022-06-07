import logging
import tkinter as tk
from tkinter.filedialog import askdirectory


class __FolderPickWindow:
    """Wrapper class for a simple folder selection gui"""

    def __init__(self, windowtitle, initial_dir):
        """Initial setup of all variables"""
        self.windowtitle = windowtitle
        self.initial_dir = initial_dir
        self.window = None
        self.selected_path = None
        return

    def show(self):
        """Creates the gui, shows it to the user and may retrive the folder path of a selected folder"""
        self.selected_path = None
        self.window = tk.Tk()
        self.window.withdraw()
        self.selected_path = askdirectory(title=self.windowtitle,
                                          initialdir=self.initial_dir)
        return


def __main():
    logging.basicConfig(level=logging.INFO)
    print(get_folderpath_from_user("Test", ))


def get_folderpath_from_user(windowtitle: str, initial_directory='/'):
    """
    Returns a folder path, which can be choosen by the user via gui.

    :param windowtitle: Defines the name of the window.
    :param initial_directory: Path of the initialy opend folder.
    :return: filepath: Path of the file, selected by the user. Returns False if no file was choosen.
    """
    logger = logging.getLogger("get_folderpath_from_user")
    logger.log(logging.INFO, "get_folderpath_from_user() is called")

    if not isinstance(windowtitle, str):
        logger.log(logging.ERROR, f"{str(type(windowtitle))} instead of str was passed as windowtitle")
        raise TypeError("Argument 'windowtitle' was not a String")

    if not isinstance(initial_directory, str):
        logger.log(logging.ERROR, f"{str(type(initial_directory))} instead of str was passed as initial_directory")
        raise TypeError("Argument 'initial_directory' was not a String")

    fpw = __FolderPickWindow(windowtitle, initial_directory)
    fpw.show()
    folderpath = fpw.selected_path

    if folderpath == "":
        logger.log(logging.WARNING, "No file was picked")
        folderpath = False

    return folderpath


if __name__ == "__main__":
    __main()
