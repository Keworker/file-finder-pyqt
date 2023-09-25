from typing import NoReturn as Unit, Optional
from PyQt6.QtWidgets import QSizePolicy, QListWidgetItem, QListWidget, QWidget, QAbstractItemView
from PyQt6.QtCore import QSize


class ListViewNoScroll(QListWidget):  # {
    def __init__(self):  # {
        super().__init__()
        policy: QSizePolicy = self.sizePolicy()
        policy.setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.setSizePolicy(policy)
        self.__maxElemHeight: int = 0
        self.verticalScrollBar().setStyleSheet("QScrollBar {width:0;}")
        self.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
    # }

    # @Override
    def setItemWidget(self, item: Optional[QListWidgetItem], widget: Optional[QWidget]) -> Unit:  # {
        super().setItemWidget(item, widget)
        if (widget.height() > self.__maxElemHeight):  # {
            self.__maxElemHeight = widget.height()
        # }
    # }

    # @Override
    def sizeHint(self) -> QSize:  # {
        width: int = self.contentsRect().width()
        spacing: int = self.spacing() + 1
        elemHeight: int = self.__maxElemHeight
        marginsHeight: int = self.contentsMargins().top() + self.contentsMargins().bottom()
        n: int = self.count()
        return QSize(width, (spacing + elemHeight) * n + marginsHeight + 2 * n - spacing)
    # }
# }
