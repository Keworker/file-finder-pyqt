import os as OS
import platform as Platform
import subprocess as Subprocess
from typing import Any as Unit
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

from src.python.File import File
from src.res.strings import VIEW_IN_EXPLORER


class FileSearchResultItem(QWidget):  # {
    def __init__(self, file: File):  # {
        super().__init__()
        self.__file: File = file
        root: QVBoxLayout = QVBoxLayout(self)
        name: QLabel = QLabel(file.path)
        hBox: QHBoxLayout = QHBoxLayout()
        count: QLabel = QLabel(str(file.matchCount))
        content: QLabel = QLabel(file.preview)
        hBox.addWidget(count)
        hBox.addWidget(content)
        goToFile: QPushButton = QPushButton(VIEW_IN_EXPLORER)
        # noinspection PyUnresolvedReferences
        goToFile.clicked.connect(self.__onPressed)
        root.addWidget(name)
        root.addLayout(hBox)
        root.addWidget(goToFile)
    # }

    def __onPressed(self) -> Unit:  # {
        if (Platform.system() == "Windows"):  # {
            OS.startfile(self.__file.path)
        # }
        elif (Platform.system() == "Darwin"):  # {
            Subprocess.run(["open", self.__file.path], check=False)
        # }
        else:  # {
            Subprocess.run(["xdg-open", self.__file.path], check=False)
        # }
    # }
# }
