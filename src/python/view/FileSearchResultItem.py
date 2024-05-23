import os as OS
import platform as Platform
import subprocess as Subprocess
from copy import copy
from typing import NoReturn as Unit
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy

from src.python.data.File import File
from src.res.strings import VIEW_IN_EXPLORER, CANT_LOAD_PREVIEW


class FileSearchResultItem(QWidget):  # {
    def __init__(self, file: File):  # {
        super().__init__()
        self.__file: File = file
        root: QVBoxLayout = QVBoxLayout(self)
        name: QLabel = QLabel(file.path.replace("\\", "/"))
        hBox: QHBoxLayout = QHBoxLayout()
        count: QLabel = QLabel(str(file.matchCount))
        count.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        content: QLabel = QLabel()
        if (file.preview):  # {
            content.setText(file.preview)
        # }
        else:  # {
            content.setText(CANT_LOAD_PREVIEW)
        # }
        hBox.addWidget(count)
        hBox.addWidget(content)
        goToFile: QPushButton = QPushButton(VIEW_IN_EXPLORER)
        # noinspection PyUnresolvedReferences
        goToFile.clicked.connect(self.__onPressed)
        root.addWidget(name)
        root.addLayout(hBox)
        root.addWidget(goToFile)
    # }

    def getFile(self) -> File:  # {
        """
        Get copy of this item's file result.
        :return: File
        """
        return copy(self.__file)
    # }

    def __lt__(self, other):  # {
        if (isinstance(other, FileSearchResultItem)):  # {
            return self.getFile() < other.getFile()
        # }
        return True
    # }

    def __onPressed(self) -> Unit:  # {
        path: str = OS.path.dirname(self.__file.path)
        if (Platform.system() == "Windows"):  # {
            OS.startfile(path)
        # }
        elif (Platform.system() == "Darwin"):  # {
            Subprocess.run(["open", path], check=False)
        # }
        else:  # {
            Subprocess.run(["xdg-open", path], check=False)
        # }
    # }
# }
