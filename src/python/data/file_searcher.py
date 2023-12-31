import multiprocessing
from multiprocessing import Pool
from typing import NoReturn as Unit, Callable
from os import listdir as listDir
from os.path import isfile as isFile, join
import re as RegEx

import json as Json
import asyncio as AsyncIO
import requests as Requests

from src.python.data.File import File
from src.python.data.FileContentMode import FileContentMode
from src.python.data.FilenameMode import FilenameMode
from src.python.data.RemoteResult import RemoteResult

UNIVERSAL_EXTENSION: str = ".*"
SYMBOLS_FOR_PREVIEW: int = 75


def isFileMatches(path: str, fileContentMode: FileContentMode, content: str) -> int:  # {
    """
    Function for check if file matches conditions

    :param path: Path to file under check
    :param fileContentMode: Mode of check
    :param content: Content for matching
    :return: Count of matches if file is suitable, else null
    """
    try:  # {
        with open(path, "r", encoding="UTF-8") as f:  # {
            text: str = f.read()
            match fileContentMode:  # {
                case FileContentMode.PLAIN:  # {
                    if (content in text):  # {
                        return text.count(content)
                    # }
                # }
                case FileContentMode.IGNORE_WHITESPACE:  # {
                    text = RegEx.sub("\\s", "", text)
                    curContent: str = RegEx.sub("\\s", "", content)
                    if (curContent in text):  # {
                        return text.count(curContent)
                    # }
                # }
                case FileContentMode.REGEX:  # {
                    if (RegEx.match(content, text)):  # {
                        return len(RegEx.findall(content, text))
                    # }
                # }
            # }
        # }
    # }
    except (UnicodeError, PermissionError):  # {
        return 0
    # }
    except FileNotFoundError:  # {
        pass
    # }
    return None
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
        try:  # {
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
                        callback(File(
                            curPath, matchCount,
                            f.read(SYMBOLS_FOR_PREVIEW).strip() + "..."
                        ))
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
                searchLocally(
                    curPath, filename, filenameMode,
                    content, fileContentMode, callback, pool
                )
            # }
        # }
        except FileNotFoundError:  # {
            continue
        # }
    # }
# }


async def getRemoteResults(
        filename: str, content: str, organization: str, token: str,
        callback: Callable[[RemoteResult], Unit]
) -> Unit:  # {
    """
    Get files by searching at GitHub

    :param filename: ';' separated filename filter
    :param content: Query for getting content
    :param organization: GitHub account for search
    :param token: API token for GitHun
    :param callback: Callback that will be called for each result
    :return: Unit (Void (NoReturn))
    """
    filenamesFilter: str = "+OR+".join(["filename:" + it.strip() for it in filename.split(";")])
    query: str = f"?q={content.replace(' ', '+')}+{filenamesFilter}+org:{organization}"
    headers: dict[str, str] = {"Authorization": f"Bearer {token}"}
    future = AsyncIO.get_event_loop().run_in_executor(
        None, lambda: Requests.request(
            "GET", f"https://api.github.com/search/code{query}",
            headers=headers, timeout=15
        ))
    result = await future
    data = Json.loads(result.text)
    for item in data["items"] if "items" in data else []:  # {
        callback(RemoteResult(item["html_url"], item["path"]))
    # }
# }


def searchFile(
        path: str, filename: str, filenameMode: FilenameMode,
        content: str, fileContentMode: FileContentMode,
        tokenAPI: str, searchOrg: str,
        callback: Callable[[File], Unit],
        remoteCallback: Callable[[RemoteResult], Unit]
) -> Unit:  # {
    """
    Function for searching file, that organizes results from all possible search variants.

    :param path: Path to the folder where we need to search
    :param filename: Text for searching by filename
    :param filenameMode: Mode of searching by name
    :param content: Text for searching by content (nullable)
    :param tokenAPI: GitHub API token for searching
    :param searchOrg: Account for searching
    :param fileContentMode: Mode of searching by text (nullable)
    :param callback: Function that will be called after each found element
    :param remoteCallback: Function that we called after each GitHub result found
    :return: Unit (Void (NoReturn))
    """
    if (tokenAPI and searchOrg):  # {
        AsyncIO.get_event_loop().run_until_complete(getRemoteResults(
            filename, content, searchOrg, tokenAPI, remoteCallback
        ))
    # }
    with Pool(multiprocessing.cpu_count()) as pull:  # {
        searchLocally(path, filename, filenameMode, content, fileContentMode, callback, pull)
    # }
# }
