from datetime import datetime as Time
from time import sleep
from typing import NoReturn as Unit

from simple_sync_search import searchSync
from simple_multithread_search import searchMultithread
from DebuggableExecutor import DebuggableExecutor


def syncSearchCallback() -> Unit:  # {
    syncResults.append(Time.now())
# }


def asyncSearchCallback() -> Unit:  # {
    asyncResults.append(Time.now())
# }


path: str = input("Input a path of big directory, that contains a lot of .txt files with symbol 'a': ")

syncResults: list[Time] = list()
totalSyncTime: Time
start: Time = Time.now()
searchSync(path, ".txt", "a", syncSearchCallback)
totalSyncTime = Time.now() - start
print(len(syncResults))
print(f"Total time of sync searching is {totalSyncTime}")
mean: list[float] = [
    (syncResults[i] - syncResults[i - 1]).total_seconds()
    for i in range(1, len(syncResults), +1)
]
print(f"Average callback time is {sum(mean) / len(mean) if mean else 0}")
"""
Sync results for user home directory:
* Total time of sync searching is 0:04:28.469227
* Average callback time is 0.050313703655107844
"""

with DebuggableExecutor() as pool:  # {
    asyncResults: list[Time] = list()
    totalAsyncTime: Time
    start: Time = Time.now()
    pool.submit(searchMultithread, path, ".txt", "a", asyncSearchCallback, pool)
    previous: int = -1
    while (pool.counter != previous):  # {
        previous = pool.counter
        sleep(10)
    # }
    pool.shutdown(wait=True)
    totalAsyncTime = Time.now() - start
    print(len(asyncResults))
    print(f"Total time of multithread searching is {totalAsyncTime}")
    mean: list[float] = [
        (asyncResults[i] - asyncResults[i - 1]).total_seconds()
        for i in range(1, len(asyncResults), +1)
    ]
    print(f"Average callback time is {sum(mean) / len(mean) if mean else 0}")
# }
"""
Multithread results for user home directory:
* Total time of multithread searching is 0:01:10.016163
* Average callback time is 0.011966308903467698
"""
