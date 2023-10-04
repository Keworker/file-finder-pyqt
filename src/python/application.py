import sys as System
import darkdetect as DarkDetect
from PyQt6 import QtWidgets, QtCore
from qt_material import apply_stylesheet as applyStylesheet

from src.python.MainWindow import MainWindow
from src.res.drawable import APP_ICON_256, APP_ICON_1024, ASSETS_DIR, ASSETS_PLACEHOLDER
from src.res.styles import THEME_DARK, THEME_LIGHT


QtCore.QDir.addSearchPath(ASSETS_PLACEHOLDER, ASSETS_DIR)
app: QtWidgets.QApplication = QtWidgets.QApplication(System.argv)
applyStylesheet(app, theme=THEME_DARK if DarkDetect.isDark() else THEME_LIGHT)
window: MainWindow = MainWindow(app, APP_ICON_256, APP_ICON_1024)
System.exit(app.exec())
