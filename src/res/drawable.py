from pathlib import Path
import os as OS


ASSETS_PLACEHOLDER: str = "assets"
ASSETS_DIR: str = OS.path.join(str(OS.path.normpath(Path(__file__).parent)), ASSETS_PLACEHOLDER, "")
APP_ICON_256: str = f"{ASSETS_PLACEHOLDER}:icon256.ico"
APP_ICON_1024: str = f"{ASSETS_PLACEHOLDER}:icon1024.png"
