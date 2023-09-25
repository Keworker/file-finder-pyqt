from typing import NoReturn as Unit, Optional
from PyQt6.QtWidgets import QSizePolicy, QListWidgetItem, QListWidget, QWidget, QAbstractItemView
from PyQt6.QtCore import QSize


class ListViewNoScroll(QListWidget):  # {
    """
    Subclass of PyQt6.QtWidgets.QListWidget.
    It gives you opportunity to create list view without scrollbar (all elements are on screen).
    This class can be useful if you use QListWidget in scrollable area.
    """

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
    def setItemWidget(
            self,
            item: Optional[QListWidgetItem],
            widget: Optional[QWidget]
    ) -> Unit:  # {
        """
        Sets the widget to be displayed in the given item.

        :param item: QListWidgetItem
        :param widget: QWidget
        :return: Unit (Void (NoReturn))
        """
        super().setItemWidget(item, widget)
        if (widget.height() > self.__maxElemHeight):  # {
            self.__maxElemHeight = widget.height()
        # }
    # }

    # @Override
    def sizeHint(self) -> QSize:  # {
        """
        This property holds the recommended size for the widget.

        :return: Unit (Void (NoReturn))
        """
        width: int = self.contentsRect().width()
        spacing: int = self.spacing() + 1
        elemHeight: int = self.__maxElemHeight
        marginsHeight: int = self.contentsMargins().top() + self.contentsMargins().bottom()
        n: int = self.count()
        return QSize(width, (spacing + elemHeight) * n + marginsHeight + 2 * n - spacing)
    # }
# }
