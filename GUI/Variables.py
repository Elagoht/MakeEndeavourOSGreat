from PyQt5.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, QAbstractItemView, QMessageBox
from re import search


class VariableWin(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.setParent(parent)
        self.variables = {}
        self.current_value = ""

        # Create widgets
        self.tblVariables = QTableWidget()
        self.btnDelete = QPushButton("Delete", self)
        self.btnAddNew = QPushButton("Add", self)

        # Table settings
        self.tblVariables.setColumnCount(2)
        self.tblVariables.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tblVariables.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.tblVariables.setHorizontalHeaderLabels(["Variable", "Value"])

        # Link functions to buttons
        self.btnAddNew.clicked.connect(self.add_variable)
        self.btnDelete.clicked.connect(self.delete_variable)

        # Add widgets to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.tblVariables, 0, 0, 1, 2)
        self.layout.addWidget(self.btnAddNew, 1, 0)
        self.layout.addWidget(self.btnDelete, 1, 1)

        # Initialize
        self.get_environment_variables()
        self.reload_table()
        self.tblVariables.cellChanged.connect(self.change_data)
        self.tblVariables.currentCellChanged.connect(self.get_current_value)
        self.tblVariables.setCurrentCell(0, 0)

    def get_current_value(self, row, col):
        self.current_value = "" \
            if self.tblVariables.item(row, col) is None \
            else self.tblVariables.item(row, col).text()

    # Get Environment Variables
    def get_environment_variables(self):
        with open("/etc/environment", "r") as file:
            lines = file.readlines()
            for line in lines:
                # Check for format
                if search("^[a-zA-Z_][a-zA-Z0-9_]*=\S", line):
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
        length = self.tblVariables.rowCount()
        print(length)
        # Check if not already have an empty variable
        for row in range(length):
            item = self.tblVariables.item(row, 0)
            # Check if the item exists and if it contains any data
            if item is None or item.text() == "":
                return

        # Add one more row
        self.tblVariables.setRowCount(length + 1)

    def change_data(self, row, col):
        keys = list(self.variables.keys())
        values = list(self.variables.values())
        new = self.tblVariables.item(row, col).text()

        # Check if new data match with regex
        if new != "" and col != 1:
            if not search("^[a-zA-Z_][a-zA-Z0-9_]*$", new):
                self.tblVariables.setItem(
                    row, col, QTableWidgetItem(self.current_value))
                return

        # Make changes
        if col:
            if row < len(values):
                values[row] = new
            else:
                values.append(new)
        else:
            if row < len(keys):
                keys[row] = new
            else:
                keys.append(new)

        if len(values) < len(keys):
            # Placeholder value
            values.append("")
        if len(values) > len(keys):
            # Placeholder value
            keys.append("")

        # Re-assign to variable
        self.variables = dict((k, v) for k, v in zip(keys, values))
        # Check for errors
        self.check_for_unique_keys()
        # Update current value
        self.get_current_value(row, col)

        # DEBUG
        print(self.variables)
        for k, v in self.variables.items():
            print(f"{k}={v}")

    def check_for_unique_keys(self):
        # Get variable list
        row_items = []
        for row in range(self.tblVariables.rowCount()):
            row_items.append("" if self.tblVariables.item(row, 0) is None
                             else self.tblVariables.item(row, 0).text())
        # Get non-unique items
        non_unique = [item for item in row_items if row_items.count(item) > 1]

        # if non-unique values are exist, warn the user
        if non_unique:
            QMessageBox.warning(
                self,
                "Non-Unique Variable",
                "Do not use same variable names. In terms of using same variables, only the last one will be used."
            )

    def delete_variable(self):
        current = self.tblVariables.currentRow()
        if current:
            del self.variables[list(self.variables.keys())[current]]
            self.reload_table()
