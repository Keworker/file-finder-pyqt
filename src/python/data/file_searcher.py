import multiprocessing
from multiprocessing import Pool
from typing import NoReturn as Unit, Callable
from os import listdir as listDir
from os.path import isfile as isFile, join
import re as RegEx

from src.python.File import File
from src.python.FileContentMode import FileContentMode
from src.python.FilenameMode import FilenameMode

UNIVERSAL_EXTENSION: str = ".*"
SYMBOLS_FOR_PREVIEW: int = 75


def isFileMatches(path: str, fileContentMode: FileContentMode, content: str) -> int:  # {
    try:  # {
        with open(path, "r", encoding="UTF-8") as f:  # {
            text: str = f.read()
            match fileContentMode:  # {
                case FileContentMode.PLAIN:  # {
                    if not (content in text):  # {
                        return None
                    # }
                    return text.count(content)
                # }
                case FileContentMode.IGNORE_WHITESPACE:  # {
                    text = RegEx.sub("\\s", "", text)
                    curContent: str = RegEx.sub("\\s", "", text)
                    if not (curContent in text):  # {
                        return None
                    # }
                    return text.count(curContent)
                # }
                case FileContentMode.REGEX:  # {
                    if not (RegEx.match(content, text)):  # {
                        return None
                    # }
                    return len(RegEx.findall(content, text))
                # }
            # }
        # }
    # }
    except (UnicodeError, PermissionError):  # {
        return 0
    # }
    except FileNotFoundError:  # {
        return None
    # }
# }


def searchLocally(
        path: str, filename: str, filenameMode: FilenameMode,
        content: str, fileContentMode: FileContentMode,
        callback: Callable[[File], Unit], pool: Pool
) -> Unit:  # {
    """
    Function for searching file, that search it locally.

    :param path: Path to the folder where we need to search
    :param filename: Text for searching by filename
    :param filenameMode: Mode of searching by name
    :param content: Text for searching by content (nullable)
    :param fileContentMode: Mode of searching by content
    :param callback: Function that will be called after each found element
    :param pool: Multiprocessing pool for async searching
    :return: Unit (Void (NoReturn))
    """
    extensions: list[str] = None
    if (filenameMode == FilenameMode.EXTENSION):  # {
        extensions: list[str] = [it.lstrip(".") for it in filename.split(";") if it]
        if (UNIVERSAL_EXTENSION in extensions):  # {
            extensions = [UNIVERSAL_EXTENSION]
        # }
    # }
    for file in listDir(path):  # {
        curPath: str = join(path, file)
        if (isFile(curPath)):  # {
            match filenameMode:  # {
                case FilenameMode.EXTENSION:  # {
                    extension: str = file.split(".")[-1] if "." in file else ""
                    if not (extension in extensions or UNIVERSAL_EXTENSION in extensions):  # {
                        continue
                    # }
                # }
                case FilenameMode.REGEX:  # {
                    if not (RegEx.fullmatch(filename, file)):  # {
                        continue
                    # }
                # }
            # }
            matchCount: int = 0
            if (content):  # {
                temp = isFileMatches(curPath, fileContentMode, content)
                if (temp is None):  # {
                    continue
                # }
                matchCount = temp
            # }
            try:  # {
                with open(curPath, "r", encoding="UTF-8") as f:  # {
                    callback(File(curPath, matchCount, f.read(SYMBOLS_FOR_PREVIEW).strip() + "..."))
                # }
            # }
            except (UnicodeError, PermissionError):  # {
                callback(File(curPath, matchCount, None))
            # }
            except FileNotFoundError:  # {
                pass
            # }
        # }
        else:  # {
            searchLocally(curPath, filename, filenameMode, content, fileContentMode, callback, pool)
        # }
    # }
# }


def searchFile(
        path: str, filename: str, filenameMode: FilenameMode,
        content: str, fileContentMode: FileContentMode,
        callback: Callable[[File], Unit]
) -> Unit:  # {
    """
    Function for searching file, that organizes results from all possible search variants.

    :param path: Path to the folder where we need to search
    :param filename: Text for searching by filename
    :param filenameMode: Mode of searching by name
    :param content: Text for searching by content (nullable)
    :param fileContentMode: Mode of searching by text (nullable)
    :param callback: Function that will be called after each found element
    :return: Unit (Void (NoReturn))
    """
    with Pool(multiprocessing.cpu_count()) as pull:  # {
        searchLocally(path, filename, filenameMode, content, fileContentMode, callback, pull)
    # }
# }
