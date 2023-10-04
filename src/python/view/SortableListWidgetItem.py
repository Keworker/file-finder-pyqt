from PyQt6.QtWidgets import QListWidgetItem, QWidget


class SortableListWidgetItem(QListWidgetItem):  # {
    # noinspection PyTypeChecker
    def __init__(self, *args):  # {
        super().__init__(*args)
        self.widget: QWidget = None
    # }

    def __lt__(self, other):  # {
        try:  # {
            # noinspection PyUnresolvedReferences
            return self.widget > other.widget
        # }
        except AttributeError:  # {
            return True
        # }
        except TypeError:  # {
            return True
        # }
    # }
# }
