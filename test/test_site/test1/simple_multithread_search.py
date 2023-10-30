from concurrent.futures.thread import ThreadPoolExecutor
from typing import NoReturn as Unit, Callable
from os import listdir as listDir
from os.path import isfile as isFile, join


def searchMultithread(
        path: str, extension: str, content: str, callback: Callable, pool: ThreadPoolExecutor
) -> Unit:  # {
    """
    Function for searching files, that search it locally in multy thread.
    """
    for file in listDir(path):  # {
        curPath: str = join(path, file)
        if (isFile(curPath)):  # {
            try:  # {
                if (file.endswith(extension)):  # {
                    with open(curPath, "r", encoding="utf8") as data:  # {
                        if (content in data.read()):  # {
                            callback()
                        # }
                    # }
                # }
            # }
            except Exception as e:  # {
                pass
            # }
        # }
        else:  # {
            try:  # {
                pool.submit(searchMultithread, curPath, extension, content, callback, pool)
            # }
            except Exception as e:  # {
                pass
            # }
        # }
    # }
# }
