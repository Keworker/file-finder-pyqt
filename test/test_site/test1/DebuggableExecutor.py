from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Callable


class DebuggableExecutor(ThreadPoolExecutor):  # {
    def __init__(self, *args, **kwargs):  # {
        super().__init__(*args, **kwargs)
        self.counter: int = 0
    # }

    # @Override
    def submit(self, __fn: Callable, *args, **kwargs) -> Future:  # {
        self.counter += 1
        return super().submit(__fn, *args, **kwargs)
    # }
# }
