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
        icon: QLabel = QLabel()
        icon.setPixmap(iconLarge)
        icon.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        root.addWidget(icon)
        vBox: QVBoxLayout = QVBoxLayout()
        vBox.setAlignment(Qt.AlignmentFlag.AlignTop)
        appName: QLabel = QLabel(APP_TITLE)
        fontTitle: QFont = appName.font()
        fontTitle.setBold(1)
        fontTitle.setWeight(fontTitle.weight() * 3)
        fontTitle.setPointSize(48)
        appName.setFont(QFont(fontTitle))
        vBox.addWidget(appName)
        version: QLabel = QLabel(VERSION)
        fontVersion: QFont = version.font()
        fontVersion.setUnderline(1)
        version.setFont(QFont(fontVersion))
        vBox.addWidget(version)
        about: QLabel = QLabel(ABOUT_TEXT)
        about.setMaximumWidth(shape.width() - iconLarge.width())
        about.setWordWrap(1)
        vBox.addWidget(about)
        link: QLabel = QLabel(REPO_LINK)
        link.setOpenExternalLinks(1)
        link.setMaximumWidth(shape.width() - iconLarge.width())
        vBox.addWidget(link)
        contacts: QLabel = QLabel(CONTACTS)
        contacts.setAlignment(Qt.AlignmentFlag.AlignBottom)
        contacts.setOpenExternalLinks(1)
        contacts.setMaximumWidth(shape.width() - iconLarge.width())
        vBox.addWidget(contacts)
        root.addLayout(vBox)
        self.setWindowTitle(ABOUT_TITLE)
        self.setWindowIcon(iconSmall)
        shape.moveCenter(screen.center())
        self.setGeometry(shape)
        self.showNormal()
    # }
# }
