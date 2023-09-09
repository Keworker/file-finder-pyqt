from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtGui import QIcon
from typing import NoReturn as Unit


class MainWindow(QWidget):  # {
    def __init__(self, title: str, iconPath: str):  # {
        super().__init__()
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(iconPath))
        self.__initWidgets()
    # }

    def __initWidgets(self) -> Unit:  # {
        # TODO:
        #  We should init our widgets here. They are:
        #  1. Title
        #  2. Radio group file mask / regex
        #  3. Edit text for files search rules
        #  4. Checkbox search in body
        #  5. Radio group simple search / ignore spaces / regex
        #  6. Large edit text for searching in body
        #  7. Log in with GitHub button - just addition feature
        #  8. Repository for searching (author/repo-name) - just addition feature
        #  9. List with results
        pass
    # }
# }
