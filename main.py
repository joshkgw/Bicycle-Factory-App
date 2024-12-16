from dataclasses import dataclass
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Greener-Bikes Bicycle Factory")

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()

        page_layout.addLayout(button_layout)    #Nest horizontal layout inside vertical layout, for the menu buttons
        page_layout.addLayout(self.stack_layout)    #Nests stacked layout inside vertical layout

        # Tabbed menu using push buttons
        self.create_menu_tab(button_layout, "Dashboard", "red", self.activate_menu_1)
        self.create_menu_tab(button_layout, "Inventory", "green", self.activate_menu_2)
        self.create_menu_tab(button_layout, "Orders", "blue", self.activate_menu_3)
        self.create_menu_tab(button_layout, "Save", "yellow", self.activate_menu_4)

        # Apply layout to the window
        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def create_menu_tab(self, button_layout, name: str, container, destination):
        """Creates buttons for each tab in the menu

        Arguments:
        button_layout: location for buttons to be placed
        name: text to be displayed on the button
        container: the widget to be displayed in the stacked layout once the button is pressed
        destination: the function to be called when the button is pressed
        """
        btn = QPushButton(name)
        btn.pressed.connect(destination)    # Destination should correspond to an appropriate activate_menu_x()
        button_layout.addWidget(btn)    # Nests button inside button layout
        self.stack_layout.addWidget(Color(container))

    def activate_menu_1(self):
        """Activates the dashboard tab"""
        self.stack_layout.setCurrentIndex(0)

    def activate_menu_2(self):
        """Activates the inventory tab"""
        self.stack_layout.setCurrentIndex(1)

    def activate_menu_3(self):
        """Activates the orders tab"""
        self.stack_layout.setCurrentIndex(2)

    def activate_menu_4(self):
        """Prompts the user to save the program"""
        confirmation = QMessageBox.question(
            self,
            "Save",
            "Are you sure that you would like to save the program?"
        )

        # Save functionality not implemented, so pass
        if confirmation.Yes:
            pass
        else:
            pass


class Color(QWidget):
    """Takes a colour as a parameter and instantiates an object containing a solid colour widget"""
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


def main():
    # Instantiates application event loop
    app = QApplication(sys.argv)

    # Instantiates window object and reveals it
    window = MainWindow()
    window.show()

    # Begins application event loop
    app.exec()


if __name__ == '__main__':
    main()