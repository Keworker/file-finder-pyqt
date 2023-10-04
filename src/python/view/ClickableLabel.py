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
        """
        Add listener of clicks for label.

        :param listener: Function that will be called on click.
        :return: Unit (Void (NoReturn))
        """
        self.__listener = listener
    # }

    # @Override
    def mouseReleaseEvent(self, ev: QMouseEvent) -> Unit:  # {
        """
        Handler of mouse release event (the end of click).

        :param ev: mouse event that affects
        :return:
        """
        super().mouseReleaseEvent(ev)
        if (self.__listener):  # {
            self.clickResult = self.__listener()
        # }
    # }
# }
