from dataclasses import dataclass as Data


@Data
class File:  # {
    path: str
    matchCount: int
    preview: str

    def __lt__(self, other):  # {
        return (self.matchCount, self.path) < (other.matchCount, other.path)
    # }
# }
