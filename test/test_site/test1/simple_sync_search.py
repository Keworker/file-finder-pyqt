from typing import NoReturn as Unit, Callable
from os import listdir as listDir
from os.path import isfile as isFile, join


def searchSync(path: str, extension: str, content: str, callback: Callable) -> Unit:  # {
    """
    Function for searching files, that search it locally in single thread.
    """
    for file in listDir(path):  # {
        curPath: str = join(path, file)
        if (isFile(curPath)):  # {
            if (file.endswith(extension)):  # {
                with open(curPath, "r", encoding="utf8") as data:  # {
                    try:  # {
                        if (content in data.read()):  # {
                            callback()
                        # }
                    # }
                    except Exception:  # {
                        pass
                    # }
                # }
            # }
        # }
        else:  # {
            try:  # {
                searchSync(curPath, extension, content, callback)
            # }
            except Exception:  # {
                pass
            # }
        # }
    # }
# }
