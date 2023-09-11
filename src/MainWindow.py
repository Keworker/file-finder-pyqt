from PyQt6.QtCore import Qt, QObject
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLayout, QLabel, QScrollArea, QWidget, QLineEdit, \
    QRadioButton, QTextEdit, QCheckBox
from PyQt6.QtGui import QIcon, QPixmap, QFont
from typing import NoReturn as Unit, Iterable

from src.res.strings import HINT_EDIT_FILENAME, USE_EXTENSION, USE_REG_EX, APP_TITLE, HINT_EDIT_FILE_CONTENT, \
    USE_CONTENT, DEFAULT_SEARCH, IGNORE_WHITESPACE


class MainWindow(QMainWindow):  # {
    def __init__(self, iconSmallPath: str, iconLargePath: str):  # {
        super().__init__()
        self.__initWidgets(iconSmallPath, iconLargePath)
    # }

    def __initWidgets(self, iconSmallPath: str, iconLargePath: str) -> Unit:  # {
        # TODO:
        #  We should init our widgets here. They are:
        #  1. DONE: Title
        #  2. DONE: Radio group file mask / regex
        #  3. DONE: Edit text for files search rules
        #  4. DONE: Checkbox search in body
        #  5. Half-done: Radio group simple search / ignore spaces / regex
        #  6. DONE: Large edit text for searching in body
        #  7. Log in with GitHub button - just addition feature
        #  8. Repository for searching (author/repo-name) - just addition feature
        #  9. List with results
        #  10. Select directory to search
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(1)
        self.widget = QWidget()
        root: QVBoxLayout = QVBoxLayout(self.widget)
        root.setAlignment(Qt.AlignmentFlag.AlignTop)
        root.addLayout(self.__getTitleLayout(APP_TITLE, iconLargePath))
        self.__addAll(root, self.__getFilenameEditor())
        self.__addAll(root, self.__getContentEditor())
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        self.setWindowTitle(APP_TITLE)
        self.setWindowIcon(QIcon(iconSmallPath))
        self.showMaximized()
    # }

    # noinspection PyUnresolvedReferences
    @staticmethod
    def __addAll(context: QLayout, elements: Iterable[QObject]) -> Unit:  # {
        for it in elements:  # {
            if (isinstance(it, QLayout)):  # {
                context.addLayout(it)
            # }
            else:  # {
                context.addWidget(it)
            # }
        # }
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

    def __getFilenameEditor(self) -> Iterable[QObject]:  # {
        self.__filenameEditor: QLineEdit = QLineEdit()
        self.__filenameEditor.setPlaceholderText(HINT_EDIT_FILENAME)
        buttonGroup: QHBoxLayout = QHBoxLayout()
        self.__extensionRadio: QRadioButton = QRadioButton(USE_EXTENSION)
        self.__extensionRadio.click()
        self.__regExRadio: QRadioButton = QRadioButton(USE_REG_EX)
        buttonGroup.addWidget(self.__extensionRadio)
        buttonGroup.addWidget(self.__regExRadio)
        return [self.__filenameEditor, buttonGroup]
    # }

    def __getContentEditor(self) -> Iterable[QObject]:  # {
        self.__fileContentEditor: QTextEdit = QTextEdit()
        self.__fileContentEditor.setPlaceholderText(HINT_EDIT_FILE_CONTENT)
        self.__useContentCheckbox: QCheckBox = QCheckBox(USE_CONTENT)
        # noinspection PyUnresolvedReferences
        self.__useContentCheckbox.stateChanged.connect(self.__onCheckboxStateChanged)
        buttonGroup: QHBoxLayout = QHBoxLayout()
        self.__defaultRadio: QRadioButton = QRadioButton(DEFAULT_SEARCH)
        self.__defaultRadio.click()
        self.__ignoreWhitespaceRadio: QRadioButton = QRadioButton(IGNORE_WHITESPACE)
        self.__regExContentRadio: QRadioButton = QRadioButton(USE_REG_EX)
        buttonGroup.addWidget(self.__defaultRadio)
        buttonGroup.addWidget(self.__ignoreWhitespaceRadio)
        buttonGroup.addWidget(self.__regExContentRadio)
        self.__onCheckboxStateChanged(False)  # TODO: Make radio groups separated
        return [self.__useContentCheckbox, buttonGroup, self.__fileContentEditor]
    # }

    def __onCheckboxStateChanged(self, state: bool) -> Unit:  # {
        self.__fileContentEditor.setReadOnly(not state)
        self.__defaultRadio.setVisible(state)
        self.__ignoreWhitespaceRadio.setVisible(state)
        self.__regExContentRadio.setVisible(state)
        self.__fileContentEditor.setVisible(state)
    # }
# }
