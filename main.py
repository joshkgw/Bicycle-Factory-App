import inspect
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

        self.currentComponentsLabel = QLabel("")

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

        complete_partial_frame = QPushButton("Complete frame welding - 1 partial frame (requires: 1 tubular steel)")
        complete_fork = QPushButton("Complete fork welding - 1 fork (requires: 1 tubular steel)")
        complete_complete_frame = QPushButton("Complete front fork assembly - 1 complete frame (requires: 1 partial frame, 1 fork)")
        complete_paint = QPushButton("Complete painting (requires: 1 paint)")
        complete_pedal = QPushButton("Complete pedal assembly (requires: 1 pedal)")
        complete_wheel = QPushButton("Complete wheel assembly (requires: 1 wheel)")
        complete_gear = QPushButton("Complete gear assembly (requires: 1 gear)")
        complete_brake = QPushButton("Complete brake assembly (requires: 1 brake)")
        complete_light = QPushButton("Complete light assembly (requires: 1 light)")
        complete_seat = QPushButton("Complete seat assembly (requires: 1 seat)")

        layout.addWidget(complete_partial_frame)
        layout.addWidget(complete_fork)
        layout.addWidget(complete_complete_frame)
        layout.addWidget(complete_paint)
        layout.addWidget(complete_pedal)
        layout.addWidget(complete_wheel)
        layout.addWidget(complete_gear)
        layout.addWidget(complete_brake)
        layout.addWidget(complete_light)
        layout.addWidget(complete_seat)

        complete_partial_frame.clicked.connect(self.handleCompletePartialFrame)
        complete_fork.clicked.connect(self.handleCompleteFork)
        complete_complete_frame.clicked.connect(self.handleCompleteCompleteFrame)
        complete_paint.clicked.connect(self.handleCompletePaint)
        complete_pedal.clicked.connect(self.handleCompletePedal)
        complete_wheel.clicked.connect(self.handleCompleteWheel)
        complete_gear.clicked.connect(self.handleCompleteGear)
        complete_brake.clicked.connect(self.handleCompleteBrake)
        complete_light.clicked.connect(self.handleCompleteLight)
        complete_seat.clicked.connect(self.handleCompleteSeat)

        dashboard_tab.setLayout(layout)
        return dashboard_tab


    def handleCompletePartialFrame(self):
        self.useComponent("tubular_steel")
        self.restockAndUpdate("partial_frame", 1)


    def handleCompleteFork(self):
        self.useComponent("tubular_steel")
        self.restockAndUpdate("fork", 1)


    def handleCompleteCompleteFrame(self):
        self.useComponent("partial_frame")
        self.useComponent("fork")
        self.restockAndUpdate("complete_frame", 1)


    def handleCompletePaint(self):
        self.useComponent("paint")


    def handleCompletePedal(self):
        self.useComponent("pedal")


    def handleCompleteWheel(self):
        self.useComponent("wheel")


    def handleCompleteGear(self):
        self.useComponent("gear")


    def handleCompleteBrake(self):
        self.useComponent("brake")


    def handleCompleteLight(self):
        self.useComponent("light")


    def handleCompleteSeat(self):
        self.useComponent("seat")


    def useComponent(self, component_name):
        # Use the specified component
        self.inventory.useComponent(component_name)
        # Fetch the updated components information
        updated_components = self.inventory.getComponents()
        # Update the QLabel with new information
        self.currentComponentsLabel.setText(updated_components)


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
        self.currentComponents = self.inventory.getComponents()
        self.currentComponentsLabel.setText(self.currentComponents)

        stat_layout.addWidget(self.currentComponentsLabel)

        # Top left: Restock buttons
        # Create buttons for restocking components
        restock_tubular_steel = QPushButton("Restock Tubular Steel")
        restock_partial_frame = QPushButton("Restock Partial Frame")
        restock_fork = QPushButton("Restock Fork")
        restock_complete_frame = QPushButton("Restock Complete Frame")
        restock_paint = QPushButton("Restock Paint")
        restock_pedal = QPushButton("Restock Pedal")
        restock_wheel = QPushButton("Restock Wheel")
        restock_gear = QPushButton("Restock Gear")
        restock_brake = QPushButton("Restock Brake")
        restock_light = QPushButton("Restock Light")
        restock_seat = QPushButton("Restock Seat")

        # Connect buttons
        restock_tubular_steel.clicked.connect(lambda: self.restockAndUpdate("tubular_steel", 5))
        restock_partial_frame.clicked.connect(lambda: self.restockAndUpdate("partial_frame", 5))
        restock_fork.clicked.connect(lambda: self.restockAndUpdate("fork", 5))
        restock_complete_frame.clicked.connect(lambda: self.restockAndUpdate("complete_frame", 5))
        restock_paint.clicked.connect(lambda: self.restockAndUpdate("paint", 5))
        restock_pedal.clicked.connect(lambda: self.restockAndUpdate("pedal", 5))
        restock_wheel.clicked.connect(lambda: self.restockAndUpdate("wheel", 5))
        restock_gear.clicked.connect(lambda: self.restockAndUpdate("gear", 5))
        restock_brake.clicked.connect(lambda: self.restockAndUpdate("brake", 5))
        restock_light.clicked.connect(lambda: self.restockAndUpdate("light", 5))
        restock_seat.clicked.connect(lambda: self.restockAndUpdate("seat", 5))

        # Add buttons to stat_layout
        restock_layout.addWidget(restock_tubular_steel)
        restock_layout.addWidget(restock_partial_frame)
        restock_layout.addWidget(restock_fork)
        restock_layout.addWidget(restock_complete_frame)
        restock_layout.addWidget(restock_paint)
        restock_layout.addWidget(restock_pedal)
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


    def restockAndUpdate(self, component_name, quantity):
        # Restock the specified component
        self.inventory.restockComponent(component_name, quantity)
        # Fetch the updated components information
        updated_components = self.inventory.getComponents()
        # Update the QLabel with new information
        self.currentComponentsLabel.setText(updated_components)


    def orderTabUI(self):
        """Create the Order page UI."""
        order_tab = QWidget()
        # Create top-level layout
        layout = QVBoxLayout()

        self.buyer_name = QLineEdit("Enter your full name.")
        self.buyer_address = QLineEdit("Enter your delivery address.")
        self.buyer_email = QLineEdit("Enter your email address.")

        self.bike_size = QComboBox()
        self.bike_size.addItems(["Small", "Medium", "Large", "Extra Large"])
        self.bike_colour = QComboBox()
        self.bike_colour.addItems(["Red", "Blue", "Green", "Yellow", "Black", "White"])
        self.bike_wheel_size = QComboBox()
        self.bike_wheel_size.addItems(["26 inch", "27.5 inch", "29 inch"])
        self.bike_gear_type = QComboBox()
        self.bike_gear_type.addItems(["Standard", "Premium"])
        self.bike_brake_type = QComboBox()
        self.bike_brake_type.addItems(["Disk", "Rim"])
        self.bike_light_type = QComboBox()
        self.bike_light_type.addItems(["Standard", "LED"])

        self.confirm_order = QPushButton("Create Order")

        layout.addWidget(self.buyer_name)
        layout.addWidget(self.buyer_address)
        layout.addWidget(self.buyer_email)

        layout.addWidget(self.bike_size)
        layout.addWidget(self.bike_colour)
        layout.addWidget(self.bike_wheel_size)
        layout.addWidget(self.bike_gear_type)
        layout.addWidget(self.bike_brake_type)
        layout.addWidget(self.bike_light_type)

        layout.addWidget(self.confirm_order)

        self.confirm_order.clicked.connect(self.createOrder)


        order_tab.setLayout(layout)
        return order_tab


    def createOrder(self):
        self.new_order = Order(
            name = self.buyer_name.text(),
            delivery_address = self.buyer_address.text(),
            email_address = self.buyer_email.text(),

            frame_size = self.bike_size.currentText(),
            colour = self.bike_colour.currentText(),
            wheel_size = self.bike_wheel_size.currentText(),
            gear_type = self.bike_gear_type.currentText(),
            brake_type = self.bike_brake_type.currentText(),
            light_type = self.bike_light_type.currentText()
        )

        self.new_order.confirmOrder()


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
            "pedal": 0,
            "wheel": 0,
            "gear": 0,
            "brake": 0,
            "light": 0,
            "seat": 0,
        }


    def getComponents(self):
        """Returns a string of all components and their quantities."""
        return inspect.cleandoc(f"""
        Tubular Steel: {self.components["tubular_steel"]}
        Partial Frame: {self.components["partial_frame"]}
        Fork: {self.components["fork"]}
        Complete Frame: {self.components["complete_frame"]}
        Paint: {self.components["paint"]}
        Pedal: {self.components["pedal"]}
        Wheel: {self.components["wheel"]}
        Gear: {self.components["gear"]}
        Brake: {self.components["brake"]}
        Light: {self.components["light"]}
        Seat: {self.components["seat"]}""")


    def useComponent(self, component):
        """Uses the specified component."""
        self.components[component] -= 1


    def restockComponent(self, component, quantity):
        """Restocks the specified component by 5 units."""
        self.components[component] += quantity
    


class Order:
    def __init__(self, name, delivery_address, email_address, frame_size, colour, wheel_size, gear_type, brake_type, light_type):
        # Customer info fields
        self.name: str = name
        self.delivery_address: str = delivery_address
        self.email_address: str = email_address

        # Bike info fields
        self.frame_size: str = frame_size
        self.colour: str = colour
        self.wheel_size: str = wheel_size
        self.gear_type: str = gear_type
        self.brake_type: str = brake_type
        self.light_type: str = light_type

        # Assembly status attribute
        self. is_assembled: bool = False


    def createOrder(self):
        new_bike = ProductionLine(self.is_assembled)


    def confirmOrder(self):
        print("Order confirmed.")
        print(f"Customer: {self.name}")
        print(f"Delivery Address: {self.delivery_address}")
        print(f"Email Address: {self.email_address}")
        print(f"Frame Size: {self.frame_size}")
        print(f"Colour: {self.colour}")
        print(f"Wheel Size: {self.wheel_size}")
        print(f"Gear Type: {self.gear_type}")
        print(f"Brake Type: {self.brake_type}")
        print(f"Light Type: {self.light_type}")


class ProductionLine:
    def __init__(self, is_assembled):
        self.partial_frame_assembled: bool = False
        self.fork_assembled: bool = False
        self.complete_frame_assembled: bool = False
        self.painted: bool = False
        self.pedal_assembled: bool = False
        self.wheel_assembled: bool = False
        self.gear_assembled: bool = False
        self.brake_assembled: bool = False
        self.light_assembled: bool = False
        self.seat_assembled: bool = False
        self.is_assembled: bool = is_assembled


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