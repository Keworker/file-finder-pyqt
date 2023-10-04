from typing import NoReturn as Unit, Callable
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QLabel


class ClickableLabel(QLabel):  # {
    # noinspection PyTypeChecker
    def __init__(self, *args):  # {
        super().__init__(*args)
        self.__listener: Callable = None
        self.clickResult = None
    # }

    def setOnClickListener(self, listener: Callable) -> Unit:  # {
        self.__listener = listener
    # }

    # @Override
    def mouseReleaseEvent(self, ev: QMouseEvent) -> Unit:  # {
        super().mouseReleaseEvent(ev)
        if (self.__listener):  # {
            self.clickResult = self.__listener()
        # }
    # }
# }
