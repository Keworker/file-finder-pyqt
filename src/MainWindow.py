from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLayout, QLabel, QScrollArea, QWidget, QLineEdit, \
    QRadioButton
from PyQt6.QtGui import QIcon, QPixmap, QFont
from typing import NoReturn as Unit, Iterable

from src.res.strings import HINT_EDIT_FILENAME, USE_EXTENSION, USE_REG_EX


class MainWindow(QMainWindow):  # {
    def __init__(self, title: str, iconSmallPath: str, iconLargePath: str):  # {
        super().__init__()
        self.__initWidgets(title, iconSmallPath, iconLargePath)
    # }

    def __initWidgets(self, title: str, iconSmallPath: str, iconLargePath: str) -> Unit:  # {
        # TODO:
        #  We should init our widgets here. They are:
        #  1. DONE: Title
        #  2. DONE: Radio group file mask / regex
        #  3. DONE: Edit text for files search rules
        #  4. Checkbox search in body
        #  5. Radio group simple search / ignore spaces / regex
        #  6. Large edit text for searching in body
        #  7. Log in with GitHub button - just addition feature
        #  8. Repository for searching (author/repo-name) - just addition feature
        #  9. List with results
        self.scroll = QScrollArea()
        self.widget = QWidget()
        root: QVBoxLayout = QVBoxLayout()
        root.setAlignment(Qt.AlignmentFlag.AlignTop)
        root.addLayout(self.__getTitleLayout(title, iconLargePath))
        for it in self.__getFilenameEditor():  # {
            if (isinstance(it, QLayout)):  # {
                root.addLayout(it)
            # }
            else:  # {
                root.addWidget(it)
            # }
        # }
        self.widget.setLayout(root)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(1)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(iconSmallPath))
        self.showMaximized()
    # }

    @staticmethod
    def __getTitleLayout(title: str, iconLargePath: str) -> QLayout:  # {
        titleContainer: QHBoxLayout = QHBoxLayout()
        title: QLabel = QLabel(title)
        font: QFont = title.font()
        font.setBold(1)
        title.setFont(font)
        title.setMaximumHeight(title.fontMetrics().height() * 4)
        icon: QLabel = QLabel()
        icon.setPixmap(QPixmap(iconLargePath).scaledToHeight(title.height()))
        titleContainer.setAlignment(Qt.AlignmentFlag.AlignLeft)
        titleContainer.addWidget(icon)
        titleContainer.addWidget(title)
        return titleContainer
    # }

    def __getFilenameEditor(self) -> Iterable[QWidget]:  # {
        self.__filenameEditor: QLineEdit = QLineEdit()
        self.__filenameEditor.setPlaceholderText(HINT_EDIT_FILENAME)
        self.__filenameButtonGroup: QHBoxLayout = QHBoxLayout()
        extensionRadio: QRadioButton = QRadioButton(USE_EXTENSION)
        extensionRadio.click()
        regExRadio: QRadioButton = QRadioButton(USE_REG_EX)
        self.__filenameButtonGroup.addWidget(extensionRadio)
        self.__filenameButtonGroup.addWidget(regExRadio)
        return [self.__filenameEditor, self.__filenameButtonGroup]
    # }
# }
