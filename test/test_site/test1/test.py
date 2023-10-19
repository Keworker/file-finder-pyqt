from datetime import datetime as Time
from typing import NoReturn as Unit

from simple_sync_search import searchSync


def syncSearchCallback() -> Unit:  # {
    syncResults.append(Time.now())
# }


syncResults: list[Time] = list()
totalSyncTime: Time
path: str = input("Input a path of big directory, that contains a lot of .txt files with symbol 'a': ")
start: Time = Time.now()
searchSync(path, ".txt", "a", syncSearchCallback)
totalSyncTime = Time.now() - start
print(f"Total time of sync searching is {totalSyncTime}")
mean: list[float] = [
    (syncResults[i] - syncResults[i - 1]).total_seconds()
    for i in range(1, len(syncResults), +1)
]
print(f"Average callback time is {sum(mean) / len(mean) if mean else 0}")
"""
Sync results for user home directory: 
* Total time of sync searching is 0:04:29.944574
* Average callback time is 0.05477315567282311
"""
