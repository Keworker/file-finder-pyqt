from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLayout, QScrollArea, QWidget
from PyQt6.QtGui import QIcon, QPixmap, QFont
from typing import NoReturn as Unit


class MainWindow(QMainWindow):  # {
    def __init__(self, title: str, iconSmallPath: str, iconLargePath: str):  # {
        super().__init__()
        self.__initWidgets(title, iconSmallPath, iconLargePath)
    # }

    def __initWidgets(self, title: str, iconSmallPath: str, iconLargePath: str) -> Unit:  # {
        # TODO:
        #  We should init our widgets here. They are:
        #  1. DONE: Title
        #  2. Radio group file mask / regex
        #  3. Edit text for files search rules
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
# }
