from dataclasses import dataclass as Data

from src.python.data.RemoteResult import RemoteResult


@Data
class File:  # {
    path: str
    matchCount: int
    preview: str

    def __lt__(self, other):  # {
        if (isinstance(other, RemoteResult)):  # {
            return True
        # }
        return (self.matchCount, self.path) < (other.matchCount, other.path)
    # }
# }
