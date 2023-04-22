import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar,QListWidget, QListWidgetItem
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QToolBar for the navigation bar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Create some QAction objects for the buttons
        action1 = QAction("Button 1", self)
        action2 = QAction("Button 2", self)
        action3 = QAction("Button 3", self)

        # Add the QAction objects to the toolbar
        toolbar.addAction(action1)
        toolbar.addAction(action2)
        toolbar.addAction(action3)

        # Create a QListWidget
        self.list_widget = QListWidget()
        self.setCentralWidget(self.list_widget)

        # Add some items to the list
        for i in range(1, 11):
            item = QListWidgetItem(f"Item {i}")
            self.list_widget.addItem(item)

        # Show the main window
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
