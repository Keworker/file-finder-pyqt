import webbrowser as WebBrowser
from copy import copy
from typing import NoReturn as Unit

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from src.python.data.RemoteResult import RemoteResult
from src.res.strings import OPEN_IN_BROWSER


class RemoteResultItem(QWidget):  # {
    def __init__(self, file: RemoteResult):  # {
        super().__init__()
        self.__file: RemoteResult = file
        root: QVBoxLayout = QVBoxLayout(self)
        name: QLabel = QLabel(file.path)
        content: QLabel = QLabel(file.url)
        goToFile: QPushButton = QPushButton(OPEN_IN_BROWSER)
        # noinspection PyUnresolvedReferences
        goToFile.clicked.connect(self.__onPressed)
        root.addWidget(name)
        root.addWidget(content)
        root.addWidget(goToFile)
    # }

    def getRemoteFile(self) -> RemoteResult:  # {
        """
        Get copy of this item's remote result (file)
        :return: RemoteResult
        """
        return copy(self.__file)
    # }

    def __lt__(self, other):  # {
        if (isinstance(other, RemoteResultItem)):  # {
            return self.getRemoteFile() < other.getRemoteFile()
        # }
        return False
    # }

    def __onPressed(self) -> Unit:  # {
        WebBrowser.open(self.__file.url)
    # }
# }
