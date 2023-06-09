from PyQt5.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView
from PyQt5.QtGui import QIcon
from re import search


class VariableWin(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.setParent(parent)
        self.variables = {}

        # Create widgets
        self.tblVariables = QTableWidget()
        self.btnDelete = QPushButton("Delete", self)
        self.btnAddNew = QPushButton("Add", self)

        # Table settings
        self.tblVariables.setColumnCount(2)
        self.tblVariables.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tblVariables.setHorizontalHeaderLabels(["Variable", "Value"])

        # Link functions to buttons
        self.btnAddNew.clicked.connect(self.add_variable)

        # Add widgets to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.tblVariables, 0, 0, 1, 2)
        self.layout.addWidget(self.btnAddNew, 1, 0)
        self.layout.addWidget(self.btnDelete, 1, 1)

        # Initialize
        self.get_environment_variables()
        self.reload_table()

    # Get Environment Variables
    def get_environment_variables(self):
        with open("/etc/environment", "r") as file:
            lines = file.readlines()
            for line in lines:
                # Check for format
                if search("^[a-zA-Z0-9_-]+=\S", line):
                    data = line.strip().split("=")
                    self.variables[data[0]] = data[1]

    # Reload table with existing variables
    def reload_table(self):
        # Set row count
        length = len(self.variables.keys())
        self.tblVariables.setRowCount(length)
        # Fil Data
        for row, variable in enumerate(self.variables.keys()):
            self.tblVariables.setItem(row, 0, QTableWidgetItem(variable))
        for row, value in enumerate(self.variables.values()):
            self.tblVariables.setItem(row, 1, QTableWidgetItem(value))

    def add_variable(self):
        # Check if not already have an empty variable
        for row in range(self.tblVariables.rowCount()):
            item = self.tblVariables.item(row, 0)
            # Check if the item exists and if it contains any data
            if item is None or item.text() == "":
                return

        # Add one more row
        length = len(self.variables.keys()) + 1
        self.tblVariables.setRowCount(length)
