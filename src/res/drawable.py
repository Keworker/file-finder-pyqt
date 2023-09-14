from pathlib import Path
import os as OS


__ASSETS_DIR: str = OS.path.join(str(Path(__file__).parent), "assets")
APP_ICON_256: str = OS.path.join(__ASSETS_DIR, "icon256.ico")
APP_ICON_1024: str = OS.path.join(__ASSETS_DIR, "icon1024.png")
