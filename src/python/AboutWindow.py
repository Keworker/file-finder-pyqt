from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QGuiApplication, QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout

from src.res.strings import ABOUT_TITLE, APP_TITLE, VERSION, ABOUT_TEXT, REPO_LINK, CONTACTS


class AboutWindow(QWidget):  # {
    def __init__(self, application: QGuiApplication, iconSmall: QIcon, iconLarge: QPixmap):  # {
        super().__init__()
        shape: QRect = self.frameGeometry()
        screen: QRect = application.primaryScreen().availableGeometry()
        shape.setWidth(screen.width() // 2)
        shape.setHeight(screen.height() // 2)
        root: QHBoxLayout = QHBoxLayout(self)
        iconLarge = iconLarge.scaled(int(shape.height() * 0.85), int(shape.height() * 0.85))
        root.addWidget(self.__getIcon(iconLarge))
        vBox: QVBoxLayout = QVBoxLayout()
        vBox.setAlignment(Qt.AlignmentFlag.AlignTop)
        vBox.addWidget(self.__getAppName())
        vBox.addWidget(self.__getVersion())
        vBox.addWidget(self.__getTextAbout(shape.width() - iconLarge.width()))
        vBox.addWidget(self.__getLink(shape.width() - iconLarge.width()))
        vBox.addWidget(self.__getContacts(shape.width() - iconLarge.width()))
        root.addLayout(vBox)
        self.setWindowTitle(ABOUT_TITLE)
        self.setWindowIcon(iconSmall)
        shape.moveCenter(screen.center())
        self.setGeometry(shape)
        self.showNormal()
    # }

    @staticmethod
    def __getIcon(iconLarge: QIcon) -> QWidget:  # {
        icon: QLabel = QLabel()
        icon.setPixmap(iconLarge)
        icon.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return icon
    # }

    @staticmethod
    def __getAppName() -> QWidget:  # {
        appName: QLabel = QLabel(APP_TITLE)
        fontTitle: QFont = appName.font()
        fontTitle.setBold(1)
        fontTitle.setWeight(fontTitle.weight() * 3)
        fontTitle.setPointSize(48)
        appName.setFont(QFont(fontTitle))
        return appName
    # }

    @staticmethod
    def __getVersion() -> QWidget:  # {
        version: QLabel = QLabel(VERSION)
        fontVersion: QFont = version.font()
        fontVersion.setUnderline(1)
        version.setFont(QFont(fontVersion))
        return version
    # }

    @staticmethod
    def __getTextAbout(width: int) -> QWidget:  # {
        about: QLabel = QLabel(ABOUT_TEXT)
        about.setMaximumWidth(width)
        about.setWordWrap(1)
        return about
    # }

    @staticmethod
    def __getLink(width: int) -> QWidget:  # {
        link: QLabel = QLabel(REPO_LINK)
        link.setOpenExternalLinks(1)
        link.setMaximumWidth(width)
        return link
    # }

    @staticmethod
    def __getContacts(width: int) -> QWidget:  # {
        contacts: QLabel = QLabel(CONTACTS)
        contacts.setAlignment(Qt.AlignmentFlag.AlignBottom)
        contacts.setOpenExternalLinks(1)
        contacts.setMaximumWidth(width)
        return contacts
    # }
# }
