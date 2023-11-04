from pathlib import Path
import os as OS


ASSETS_PLACEHOLDER: str = ""
ASSETS_DIR: str = OS.path.join(str(OS.path.normpath(Path(__file__).parent)), ASSETS_PLACEHOLDER, "")
APP_ICON_256: str = "src/res/assets/icon256.ico"
APP_ICON_1024: str = "src/res/assets/icon1024.png"
