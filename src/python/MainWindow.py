from typing import NoReturn as Unit, Iterable
from PyQt6.QtCore import Qt, QObject
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, \
    QLayout, QLabel, QScrollArea, QWidget, QLineEdit, \
    QRadioButton, QTextEdit, QCheckBox, QButtonGroup, \
    QPushButton, QFileDialog, QListWidgetItem, QSizePolicy, QInputDialog
from PyQt6.QtGui import QIcon, QPixmap, QFont

from src.python.AboutWindow import AboutWindow
from src.python.data.File import File
from src.python.data.FileContentMode import FileContentMode
from src.python.view.ClickableLabel import ClickableLabel
from src.python.view.FileSearchResultItem import FileSearchResultItem
from src.python.data.FilenameMode import FilenameMode
from src.python.view.ListViewNoScroll import ListViewNoScroll
from src.python.data.file_searcher import searchFile
from src.python.view.SortableListWidgetItem import SortableListWidgetItem
from src.res.strings import HINT_EDIT_FILENAME, USE_EXTENSION, USE_REG_EX, \
    APP_TITLE, HINT_EDIT_FILE_CONTENT, \
    USE_CONTENT, DEFAULT_SEARCH, IGNORE_WHITESPACE, SEARCH_FOR_FILES, SELECT_DIRECTORY, USE_GITHUB, LOGIN_GITHUB, \
    ACCOUNT_FOR_SEARCHING, EDIT_TOKEN, YOUR_GITHUB_API_TOKEN


class MainWindow(QScrollArea):  # {
    def __init__(self, application, iconSmallPath: str, iconLargePath: str):  # {
        super().__init__()
        self.application = application
        self.__initWidgets(iconSmallPath, iconLargePath)
    # }

    def __initWidgets(self, iconSmallPath: str, iconLargePath: str) -> Unit:  # {
        self.__token = None  # Will be deleted with "Add SQLite DB #12"

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.widget = QWidget()
        root: QVBoxLayout = QVBoxLayout(self.widget)
        root.setAlignment(Qt.AlignmentFlag.AlignTop)
        root.addLayout(self.__getTitleLayout(APP_TITLE, iconSmallPath, iconLargePath))
        self.__addAll(root, self.__getFilenameEditor(root))
        self.__addAll(root, self.__getContentEditor(root))
        self.__addAll(root, self.__getGitHubEditor())
        root.addWidget(self.__getSearchButton())
        root.addWidget(self.__getSearchResultsList())
        self.setWidget(self.widget)
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

    def __getTitleLayout(self, title: str, iconSmallPath: str, iconLargePath: str) -> QLayout:  # {
        titleContainer: QHBoxLayout = QHBoxLayout()
        title: QLabel = QLabel(title)
        font: QFont = title.font()
        font.setBold(1)
        title.setFont(font)
        title.setMaximumHeight(title.fontMetrics().height() * 4)
        icon: ClickableLabel = ClickableLabel()
        pixmap: QPixmap = QPixmap(iconLargePath)
        icon.setPixmap(pixmap.scaledToHeight(title.height()))
        icon.setOnClickListener(
            lambda: AboutWindow(self.application, QIcon(iconSmallPath), pixmap)
        )
        titleContainer.setAlignment(Qt.AlignmentFlag.AlignLeft)
        titleContainer.addWidget(icon)
        titleContainer.addWidget(title)
        return titleContainer
    # }

    def __getPathDialog(self) -> str:  # {
        return QFileDialog.getExistingDirectory(self, SELECT_DIRECTORY)
    # }

    def __getFilenameEditor(self, context: QLayout) -> Iterable[QObject]:  # {
        self.__filenameEditor: QLineEdit = QLineEdit()
        self.__filenameEditor.setPlaceholderText(HINT_EDIT_FILENAME)
        buttonGroup: QHBoxLayout = QHBoxLayout()
        radioGroup: QButtonGroup = QButtonGroup(context)
        self.__extensionRadio: QRadioButton = QRadioButton(USE_EXTENSION)
        self.__extensionRadio.click()
        self.__regExRadio: QRadioButton = QRadioButton(USE_REG_EX)
        radioGroup.addButton(self.__extensionRadio)
        radioGroup.addButton(self.__regExRadio)
        buttonGroup.addWidget(self.__extensionRadio)
        buttonGroup.addWidget(self.__regExRadio)
        return [self.__filenameEditor, buttonGroup]
    # }

    def __getContentEditor(self, context: QLayout) -> Iterable[QObject]:  # {
        self.__fileContentEditor: QTextEdit = QTextEdit()
        policy: QSizePolicy = self.__fileContentEditor.sizePolicy()
        policy.setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.__fileContentEditor.setPlaceholderText(HINT_EDIT_FILE_CONTENT)
        self.__useContentCheckbox: QCheckBox = QCheckBox(USE_CONTENT)
        # noinspection PyUnresolvedReferences
        self.__useContentCheckbox.stateChanged.connect(self.__onCheckboxStateChanged)
        buttonGroup: QHBoxLayout = QHBoxLayout()
        radioGroup: QButtonGroup = QButtonGroup(context)
        self.__defaultRadio: QRadioButton = QRadioButton(DEFAULT_SEARCH)
        self.__defaultRadio.click()
        self.__ignoreWhitespaceRadio: QRadioButton = QRadioButton(IGNORE_WHITESPACE)
        self.__regExContentRadio: QRadioButton = QRadioButton(USE_REG_EX)
        radioGroup.addButton(self.__defaultRadio)
        radioGroup.addButton(self.__ignoreWhitespaceRadio)
        radioGroup.addButton(self.__regExContentRadio)
        buttonGroup.addWidget(self.__defaultRadio)
        buttonGroup.addWidget(self.__ignoreWhitespaceRadio)
        buttonGroup.addWidget(self.__regExContentRadio)
        self.__onCheckboxStateChanged(False)
        return [self.__useContentCheckbox, buttonGroup, self.__fileContentEditor]
    # }

    def __getGitHubEditor(self) -> Iterable[QObject]:  # {
        self.__useGitHubCheckbox: QCheckBox = QCheckBox(USE_GITHUB)
        # noinspection PyUnresolvedReferences
        self.__useGitHubCheckbox.stateChanged.connect(self.__onGitHubStateChanged)
        self.__logInGitHub: QPushButton = QPushButton(LOGIN_GITHUB)
        # noinspection PyUnresolvedReferences
        self.__logInGitHub.clicked.connect(self.__showGitHubLoginDialog)
        self.__accountForSearch: QLineEdit = QLineEdit()
        self.__accountForSearch.setPlaceholderText(ACCOUNT_FOR_SEARCHING)
        self.__logInGitHub.setVisible(False)
        self.__accountForSearch.setVisible(False)
        return [self.__useGitHubCheckbox, self.__logInGitHub, self.__accountForSearch]
    # }

    def __getSearchButton(self) -> QWidget:  # {
        self.__searchButton: QPushButton = QPushButton(SEARCH_FOR_FILES)
        # noinspection PyUnresolvedReferences
        self.__searchButton.clicked.connect(self.__onSearchPressed)
        return self.__searchButton
    # }

    def __getSearchResultsList(self) -> QWidget:  # {
        self.__resultsList: ListViewNoScroll = ListViewNoScroll()
        self.__resultsList.setSortingEnabled(True)
        policy: QSizePolicy = self.__resultsList.sizePolicy()
        policy.setVerticalPolicy(QSizePolicy.Policy.Maximum)
        return self.__resultsList
    # }

    # pylint: disable=unused-private-member
    def __addFileToList(self, file: File) -> Unit:  # {
        listItem: QListWidgetItem = SortableListWidgetItem(self.__resultsList)
        customItem: FileSearchResultItem = FileSearchResultItem(file)
        listItem.setSizeHint(customItem.sizeHint())
        self.__resultsList.addItem(listItem)
        self.__resultsList.setItemWidget(listItem, customItem)
        self.__resultsList.setFixedHeight(self.__resultsList.sizeHint().height())
        self.__resultsList.sortItems()
    # }

    def __onCheckboxStateChanged(self, state: bool) -> Unit:  # {
        self.__fileContentEditor.setReadOnly(not state)
        self.__defaultRadio.setVisible(state)
        self.__ignoreWhitespaceRadio.setVisible(state)
        self.__regExContentRadio.setVisible(state)
        self.__fileContentEditor.setVisible(state)
    # }

    def __onGitHubStateChanged(self, state: bool) -> Unit:  # {
        self.__logInGitHub.setVisible(state)
        self.__accountForSearch.setVisible(state)
        if (state):  # {
            self.__extensionRadio.click()
            self.__ignoreWhitespaceRadio.click()
        # }
    # }

    def __showGitHubLoginDialog(self) -> Unit:  # {
        text, success = QInputDialog().getText(
            self,
            EDIT_TOKEN,
            YOUR_GITHUB_API_TOKEN
        )
        if (success and text):  # {
            self.__token = text  # Temp, until "Add SQLite DB #12"
        # }
    # }

    # noinspection PyTypeChecker
    def __onSearchPressed(self) -> Unit:  # {
        if (self.__useGitHubCheckbox.isChecked()):  # {
            self.__extensionRadio.click()
            self.__ignoreWhitespaceRadio.click()
        # }
        path: str = self.__getPathDialog()
        filename: str = self.__filenameEditor.text()
        filenameMode: FilenameMode
        if (self.__extensionRadio.isChecked()):  # {
            filenameMode = FilenameMode.EXTENSION
        # }
        if (self.__regExRadio.isChecked()):  # {
            filenameMode = FilenameMode.REGEX
        # }
        content: str = None
        fileContentMode: FileContentMode = None
        if (self.__useContentCheckbox.checkState()):  # {
            content = self.__fileContentEditor.toPlainText()
            if (self.__defaultRadio.isChecked()):  # {
                fileContentMode = FileContentMode.PLAIN
            # }
            if (self.__ignoreWhitespaceRadio.isChecked()):  # {
                fileContentMode = FileContentMode.IGNORE_WHITESPACE
            # }
            if (self.__regExContentRadio.isChecked()):  # {
                fileContentMode = FileContentMode.REGEX
            # }
        # }
        if (path):  # {
            self.__resultsList.clear()
            searchFile(
                path, filename, filenameMode,
                content, fileContentMode,
                self.__token, self.__accountForSearch.text(),
                self.__addFileToList
            )
        # }
    # }
# }
