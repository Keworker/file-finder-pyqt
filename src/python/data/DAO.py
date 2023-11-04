import sqlite3 as SQLite
from sqlite3 import Connection, Cursor
from typing import Any as Unit
from datetime import datetime as LocalDateTime


class DAO:  # {
    def __init__(self, path: str):  # {
        self.__path: str = path
        self.__ensureCreated()
    # }

    def addToken(self, token: str) -> Unit:  # {
        """
        Add token for GitHub API
        :param token: Token to be added
        :return: Unit (Void (NoReturn))
        """
        connection: Connection = SQLite.connect(self.__path)
        cursor: Cursor = connection.cursor()
        cursor.execute(f"INSERT INTO token VALUES (NULL, \"{token}\");")
        connection.commit()
        connection.close()
    # }

    def getToken(self) -> str:  # {
        """
        Get token for calling GitHub API
        :return: str
        """
        connection: Connection = SQLite.connect(self.__path)
        cursor: Cursor = connection.cursor()
        query = list(cursor.execute("SELECT github_token FROM token LIMIT 1;"))
        DAO.__logTokenAccess(cursor)
        connection.close()
        return query[0][0]
    # }

    def addOrganization(self, name: str) -> Unit:  # {
        """
        Add organization to history of GitHub search requests
        :param name: Name of organization
        :return: Unit (Void (NoReturn))
        """
        connection: Connection = SQLite.connect(self.__path)
        cursor: Cursor = connection.cursor()
        cursor.execute(f"INSERT OR IGNORE INTO organizations VALUES (NULL, \"{name}\");")
        connection.commit()
        connection.close()
    # }

    def getOrganizations(self) -> list[str]:  # {
        """
        Get list of organizations from history to add suggestions
        :return: list[str]
        """
        connection: Connection = SQLite.connect(self.__path)
        cursor: Cursor = connection.cursor()
        query = cursor.execute("SELECT name FROM organizations;")
        result: list[str] = [it[0] for it in query]
        connection.close()
        return result
    # }

    @staticmethod
    def __logTokenAccess(cursor: Cursor) -> Unit:  # {
        currentTime: float = LocalDateTime.now().timestamp()
        cursor.execute(f"INSERT INTO token_access VALUES (NULL, {currentTime})")
    # }

    def __ensureCreated(self) -> Unit:  # {
        connection: Connection = SQLite.connect(self.__path)
        cursor: Cursor = connection.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS "token" (
    "id"	INTEGER UNIQUE,
    "github_token"	TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);""".strip())
        cursor.execute("""
CREATE TABLE IF NOT EXISTS "token_access" (
    "id"	INTEGER UNIQUE,
    "timestamp"	INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT)
);""".strip())
        cursor.execute("""
CREATE TABLE IF NOT EXISTS "organizations" (
    "id"	INTEGER UNIQUE,
    "name"	INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT)
);""".strip())
        connection.commit()
        connection.close()
    # }
# }
