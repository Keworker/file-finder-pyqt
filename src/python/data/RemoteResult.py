from dataclasses import dataclass as Data


@Data
class RemoteResult:  # {
    url: str
    path: str

    def __lt__(self, other):  # {
        return False
    # }
# }
