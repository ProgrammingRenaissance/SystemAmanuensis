"""Testing user sapp code."""

import sys
from typing import NoReturn, Self

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from saBase import SABase
import saBase

# Flag indicating whether we were invoked from command line or not
_cl: bool = True if __name__ == '__main__' else False


class MainWindow(QMainWindow):
    """Main Qt window."""

    def __init__(self: Self) -> NoReturn:  # type: ignore
        """Initialize 'MainWindow' class."""
        saBase._result.append(saBase._STARTED_QT_INITIALIZATION)
        super().__init__()
        self.setWindowTitle('System Amanuensis')
        button = QPushButton('Press Me!')
        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(button)


class _testUc(SABase):
    def __init__(self: Self) -> NoReturn:
        """Initialize '_testUc' class."""
        saBase._result.append(saBase._STARTING_USER_CODE_INITIALIZATION)
        super().__init__()  # Calls the base class
        saBase._result.append(saBase._COMPLETED_USER_CODE_INITIALIZATION)

    def __call__(self: Self):
        app = QApplication(sys.argv)
        window: MainWindow = MainWindow()
        window.show()

        saBase._result.append(saBase._STARTING_QT_EVENT_LOOP)
        app.exec()  # Run the event loop
        # Normal application termination
        saBase._result.append(saBase._NORMAL_TERMINATION_FROM_QT)


if _cl:
    print('testUC thinks we are runnng from command line')
    # Start the sapp running
    _testUc()()  # type: ignore
    print(' \n'.join(saBase._result))
    sys.exit(saBase._ret)  # Leave Sapp
else:
    print('testUC thinks we are loading testUC as a module')
