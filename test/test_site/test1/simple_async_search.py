from multiprocessing import Pool
from typing import NoReturn as Unit, Callable
from os import listdir as listDir
from os.path import isfile as isFile, join


def searchAsync(
        path: str, extension: str, content: str, callback: Callable, pool: Pool
) -> Unit:  # {
    """
    Function for searching files, that search it locally in multy thread.
    """
    for file in listDir(path):  # {
        curPath: str = join(path, file)
        if (isFile(curPath)):  # {
            if (file.endswith(extension)):  # {
                with open(file, "r", encoding="utf8") as data:  # {
                    if (content in data.read()):  # {
                        callback()
                    # }
                # }
            # }
        # }
        else:  # {
            pool.apply_async(searchAsync, (curPath, extension, content, callback))
        # }
    # }
# }
