import inspect
from dataclasses import dataclass
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys


class DevColor(QWidget):
    """Custom Widget that sets the background to a solid color, for development purposes."""
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


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

        # Create instance of inventory
        self.inventory = Inventory()

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
        # Create top-level layout
        layout = QVBoxLayout()

        layout.addWidget(QCheckBox("Dashboard Option 1"))
        layout.addWidget(QCheckBox("Dashboard Option 2"))

        dashboard_tab.setLayout(layout)
        return dashboard_tab


    def inventoryTabUI(self):
        """Create the Inventory page UI."""
        inventory_tab = QWidget()
        # Create top-level layout
        inv_layout = QVBoxLayout()
        # Create sub-layouts
        stat_layout= QHBoxLayout()
        restock_layout = QVBoxLayout()


        # Top right: inventory List
        # Store displayComponents method in attribute and pass to QLabel
        self.currentComponents = self.inventory.displayComponents()
        self.currentComponentsLabel = QLabel(self.currentComponents)

        stat_layout.addWidget(self.currentComponentsLabel)

        # Top left: Restock buttons
        # Create buttons for restocking components
        restock_tubular_steel = QPushButton("Restock Tubular Steel")
        restock_partial_frame = QPushButton("Restock Partial Frame")
        restock_fork = QPushButton("Restock Fork")
        restock_complete_frame = QPushButton("Restock Complete Frame")
        restock_paint = QPushButton("Restock Paint")
        restock_wheel = QPushButton("Restock Wheel")
        restock_gear = QPushButton("Restock Gear")
        restock_brake = QPushButton("Restock Brake")
        restock_light = QPushButton("Restock Light")
        restock_seat = QPushButton("Restock Seat")

        # Connect buttons
        restock_tubular_steel.clicked.connect(lambda: self.restockAndUpdate("tubular_steel"))
        restock_partial_frame.clicked.connect(lambda: self.restockAndUpdate("partial_frame"))
        restock_fork.clicked.connect(lambda: self.restockAndUpdate("fork"))
        restock_complete_frame.clicked.connect(lambda: self.restockAndUpdate("complete_frame"))
        restock_paint.clicked.connect(lambda: self.restockAndUpdate("paint"))
        restock_wheel.clicked.connect(lambda: self.restockAndUpdate("wheel"))
        restock_gear.clicked.connect(lambda: self.restockAndUpdate("gear"))
        restock_brake.clicked.connect(lambda: self.restockAndUpdate("brake"))
        restock_light.clicked.connect(lambda: self.restockAndUpdate("light"))
        restock_seat.clicked.connect(lambda: self.restockAndUpdate("seat"))

        # Add buttons to stat_layout
        restock_layout.addWidget(restock_tubular_steel)
        restock_layout.addWidget(restock_partial_frame)
        restock_layout.addWidget(restock_fork)
        restock_layout.addWidget(restock_complete_frame)
        restock_layout.addWidget(restock_paint)
        restock_layout.addWidget(restock_wheel)
        restock_layout.addWidget(restock_gear)
        restock_layout.addWidget(restock_brake)
        restock_layout.addWidget(restock_light)
        restock_layout.addWidget(restock_seat)

        # Add stat layout to top-level layout
        stat_layout.addLayout(restock_layout)
        inv_layout.addLayout(stat_layout)

        #Lower widget
        inv_layout.addWidget(DevColor('blue'))

        inventory_tab.setLayout(inv_layout)
        return inventory_tab


    def restockAndUpdate(self, component_name):
        # Restock the specified component
        self.inventory.restockComponent(component_name)
        # Fetch the updated components information
        updated_components = self.inventory.displayComponents()
        # Update the QLabel with new information
        self.currentComponentsLabel.setText(updated_components)


    def orderTabUI(self):
        """Create the Order page UI."""
        order_tab = QWidget()
        # Create top-level layout
        layout = QVBoxLayout()



        layout.addWidget(QCheckBox("Order Option 2"))

        order_tab.setLayout(layout)
        return order_tab


    def saveTabUI(self):
        """Create the Save page UI"""
        save_tab = QWidget()
        # Create top-level layout
        layout = QVBoxLayout()

        # Create info label with button to save (not functional, just prints 'saved' to console)
        layout.addWidget(QLabel("Click to save your changes."))
        save_button = QPushButton("Save")
        save_button.clicked.connect(lambda: print("Saved"))
        layout.addWidget(save_button)

        layout.addStretch()
        save_tab.setLayout(layout)
        return save_tab


class Inventory:
    def __init__(self):
        self.components = {
            "tubular_steel": 0,
            "partial_frame": 0,
            "fork": 0,
            "complete_frame": 0,
            "paint": 0,
            "wheel": 0,
            "gear": 0,
            "brake": 0,
            "light": 0,
            "seat": 0,
        }

    def displayComponents(self):
        return inspect.cleandoc(f"""
        Tubular Steel: {self.components["tubular_steel"]}
        Partial Frame: {self.components["partial_frame"]}
        Fork: {self.components["fork"]}
        Complete Frame: {self.components["complete_frame"]}
        Paint: {self.components["paint"]}
        Wheel: {self.components["wheel"]}
        Gear: {self.components["gear"]}
        Brake: {self.components["brake"]}
        Light: {self.components["light"]}
        Seat: {self.components["seat"]}""")

    def restockComponent(self, component):
        self.components[component] += 5
    

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