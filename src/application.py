import sys as System
import darkdetect as DarkDetect
from PyQt6 import QtWidgets
from qt_material import apply_stylesheet as applyStylesheet

from src.MainWindow import MainWindow
from src.res.drawable import APP_ICON_256, APP_ICON_1024
from src.res.styles import THEME_DARK, THEME_LIGHT


app: QtWidgets.QApplication = QtWidgets.QApplication(System.argv)
applyStylesheet(app, theme=THEME_DARK if DarkDetect.isDark() else THEME_LIGHT)
window: MainWindow = MainWindow(APP_ICON_256, APP_ICON_1024)
app.exec()
