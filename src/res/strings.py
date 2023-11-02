APP_TITLE: str = "Finder-chan"
HINT_EDIT_FILENAME: str = ".txt;.cpp;.java"
USE_REG_EX: str = "Use regular expressions"
USE_EXTENSION: str = "Search by file extension"
USE_CONTENT: str = "Search in files content"
USE_GITHUB: str = "Search with GitHub"
IGNORE_WHITESPACE: str = "Ignore whitespace symbols"
DEFAULT_SEARCH: str = "Search full match"
HINT_EDIT_FILE_CONTENT: str = """
signed main(void) {
    signed long long int a, b;
    scanf("%lld%lld", &a, &b);
    printf("%lld", a + b);
    return 0i32;
}
""".strip()
SEARCH_FOR_FILES: str = "Start search"
SELECT_DIRECTORY: str = "Select directory for search"
VIEW_IN_EXPLORER: str = "View in file explorer"
OPEN_IN_BROWSER: str = "Open file in browser"
LOGIN_GITHUB: str = "Login into GitHub with API key"
EDIT_TOKEN: str = "Edit GitHub token"
YOUR_GITHUB_API_TOKEN: str = "Your GitHub API token:"
ACCOUNT_FOR_SEARCHING: str = "The GitHub account whose repositories you want to search for"
CANT_LOAD_PREVIEW: str = "Error while loading preview, sorry..."
ABOUT_TITLE: str = f"About '{APP_TITLE}'"
VERSION: str = "v0.0.1"
ABOUT_TEXT: str = """
Finder-chan (file finder PyQt) is a fully open source desktop app for searching files by name or content.
You can send bug report, read our licence or explore source code with our GitHub:
""".strip()
REPO_LINK: str = """
- <a href=https://github.com/Keworker/file-finder-pyqt>https://github.com/Keworker/file-finder-pyqt</a>
""".strip()
CONTACTS: str = ('If you have personal questions: '
                 '<a href="mailto:kew0rker11@gmail.com">kew0rker11@gmail.com</a>')
