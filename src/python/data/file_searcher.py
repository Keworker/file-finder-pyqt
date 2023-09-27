import multiprocessing
from multiprocessing import Pool
from typing import NoReturn as Unit, Callable
from os import listdir as listDir
from os.path import isfile as isFile, join
import re as RegEx

from src.python.File import File

UNIVERSAL_EXTENSION: str = ".*"
SYMBOLS_FOR_PREVIEW: int = 75


def searchLocally(
        path: str, filename: str, searchByExt: bool, useRegExFilename: bool,
        content: str, fullMatch: bool, ignoreWhitespace: bool, useRegExContent: bool,
        callback: Callable[[File], Unit], pool: Pool
) -> Unit:  # {
    """
    Function for searching file, that search it locally.

    :param path: Path to the folder where we need to search
    :param filename: Text for searching by filename
    :param searchByExt: Use filename param as semicolon separated possible extensions
    :param useRegExFilename: Use filename as regular expressions mask
    :param content: Text for searching by content (nullable)
    :param fullMatch: Use content for searching full match
    :param ignoreWhitespace: Use content as full match, but ignore whitespace while searching
    :param useRegExContent: Use content as regular expression mask
    :param callback: Function that will be called after each found element
    :param pool: Multiprocessing pool for async searching
    :return: Unit (Void (NoReturn))
    """
    extensions: list[str] = None
    if (searchByExt):  # {
        extensions: list[str] = filename.split(";")
        if (UNIVERSAL_EXTENSION in extensions):  # {
            extensions = [UNIVERSAL_EXTENSION]
        # }
    # }
    for file in listDir(path):  # {
        curPath: str = join(path, file)
        if (isFile(curPath)):  # {
            if (searchByExt):  # {
                extension: str = "." + file.split(".")[-1] if "." in file else ""
                if not (extension in extensions or UNIVERSAL_EXTENSION in extensions):  # {
                    continue
                # }
            # }
            elif (useRegExFilename and not RegEx.fullmatch(filename, file)):  # {
                continue
            # }
            matchCount: int = 0
            if (content is not None):  # {
                pass
            # }
            with open(curPath, "r") as f:  # {
                callback(File(curPath, matchCount, f.read(SYMBOLS_FOR_PREVIEW)))
            # }
        # }
        else:  # {
            searchLocally(
                curPath, filename, searchByExt, useRegExFilename,
                content, fullMatch, ignoreWhitespace, useRegExContent,
                callback, pool
            )
        # }
    # }
# }


def searchFile(
        path: str, filename: str, searchByExt: bool, useRegExFilename: bool,
        content: str, fullMatch: bool, ignoreWhitespace: bool, useRegExContent: bool,
        callback: Callable[[File], Unit]
) -> Unit:  # {
    """
    Function for searching file, that organizes results from all possible search variants.

    :param path: Path to the folder where we need to search
    :param filename: Text for searching by filename
    :param searchByExt: Use filename param as semicolon separated possible extensions
    :param useRegExFilename: Use filename as regular expressions mask
    :param content: Text for searching by content (nullable)
    :param fullMatch: Use content for searching full match
    :param ignoreWhitespace: Use content as full match, but ignore whitespace while searching
    :param useRegExContent: Use content as regular expression mask
    :param callback: Function that will be called after each found element
    :return: Unit (Void (NoReturn))
    """
    with Pool(multiprocessing.cpu_count()) as pull:  # {
        searchLocally(
            path, filename, searchByExt, useRegExFilename,
            content, fullMatch, ignoreWhitespace, useRegExContent,
            callback, pull
        )
    # }
# }
