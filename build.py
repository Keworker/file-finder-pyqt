import PyInstaller.__main__
import os as OS

from src.res.drawable import ASSETS_DIR, APP_ICON_256, ASSETS_PLACEHOLDER
from src.res.strings import APP_TITLE


PyInstaller.__main__.run(
    [
        OS.path.join("src", "python", "application.py"),
        "--windowed",
        "-n", APP_TITLE,
        "-i", APP_ICON_256.replace(ASSETS_PLACEHOLDER + ':', ASSETS_DIR)
    ]
)
