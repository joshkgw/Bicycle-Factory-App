from dataclasses import dataclass
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Greener-Bikes Bicycle Factory")
        self.setCentralWidget(MenuTabs())
        self.resize(800, 500)

class MenuTabs(QWidget):
    """Main window for the application"""
    def __init__(self):
        super().__init__()

        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create the tab widget with 4 tabs
        tabs = QTabWidget()
        tabs.addTab(self.dashboardTabUI(), "Dashboard")
        tabs.addTab(self.inventoryTabUI(), "Inventory")
        tabs.addTab(self.orderTabUI(), "Order")
        tabs.addTab(self.saveTabUI(), "Save")
        layout.addWidget(tabs)

    def dashboardTabUI(self):
        """Create the Dashboard page UI."""
        dashboard_tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Dashboard Option 1"))
        layout.addWidget(QCheckBox("Dashboard Option 2"))
        dashboard_tab.setLayout(layout)
        return dashboard_tab

    def inventoryTabUI(self):
        """Create the Inventory page UI."""
        inventory_tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Inventory Option 1"))
        layout.addWidget(QCheckBox("Inventory Option 2"))
        inventory_tab.setLayout(layout)
        return inventory_tab

    def orderTabUI(self):
        """Create the Order page UI."""
        order_tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Order Option 1"))
        layout.addWidget(QCheckBox("Order Option 2"))
        order_tab.setLayout(layout)
        return order_tab

    def saveTabUI(self):
        """Create the Save page UI"""
        save_tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(
            QLabel("Click to save your changes.")
        )
        save_button = QPushButton("Save")
        save_button.clicked.connect(lambda: print("Saved"))
        layout.addWidget(save_button)
        layout.addStretch()
        save_tab.setLayout(layout)
        return save_tab

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