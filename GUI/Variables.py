from PyQt5.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, QAbstractItemView, QMessageBox, QLabel
from PyQt5.QtCore import Qt
from re import search
from os import system


class VariableWin(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.setParent(parent)
        self.keys = []
        self.values = []
        self.current_value = ""

        # Create widgets
        self.lblUnrecommended = QLabel(
            "It is not recommended to set the following variables here or at all: <font face='monospace' color='red'>BROWSER, PATH, LANG, LC_*, HOME, SHELL</font>.<br/> Avoid setting these variables in this context or in general.", self)
        self.tblVariables = QTableWidget()
        self.btnAddNew = QPushButton("Add New", self)
        self.btnDelete = QPushButton("Delete Selected", self)
        self.btnSave = QPushButton("Save Changes", self)

        # Label styling
        self.lblUnrecommended.setWordWrap(True)
        self.lblUnrecommended.setTextFormat(Qt.RichText)

        # Table settings
        self.tblVariables.setColumnCount(2)
        self.tblVariables.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tblVariables.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.tblVariables.setHorizontalHeaderLabels(["Variable", "Value"])

        # Link functions to buttons
        self.btnAddNew.clicked.connect(self.add_variable)
        self.btnDelete.clicked.connect(self.delete_variable)
        self.btnSave.clicked.connect(self.save_variables)

        # Add widgets to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.lblUnrecommended, 0, 0, 1, 3)
        self.layout.addWidget(self.tblVariables, 1, 0, 1, 3)
        self.layout.addWidget(self.btnAddNew, 2, 0)
        self.layout.addWidget(self.btnDelete, 2, 1)
        self.layout.addWidget(self.btnSave, 2, 2)

        # Initialize
        self.get_environment_variables()
        self.reload_table()
        self.tblVariables.cellChanged.connect(self.change_data)
        self.tblVariables.currentCellChanged.connect(self.get_current_value)
        self.tblVariables.setCurrentCell(0, 0)

    # Get selected cell's text
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
                    self.keys.append(data[0])
                    self.values.append(data[1])

    # Reload table with existing variables
    def reload_table(self):
        # Set row count
        length = len(self.keys)
        self.tblVariables.setRowCount(length)
        # Fill data
        for row, key in enumerate(self.keys):
            self.tblVariables.setItem(row, 0, QTableWidgetItem(key))
        for row, value in enumerate(self.values):
            self.tblVariables.setItem(row, 1, QTableWidgetItem(value))

    def add_variable(self):
        length = self.tblVariables.rowCount()
        # Check if not already have an empty variable
        for row in range(length):
            item = self.tblVariables.item(row, 0)
            # Check if the item exists and if it contains any data
            if item is None or item.text() == "":
                return

        # Add one more row
        self.keys.append("")
        self.values.append("")
        self.tblVariables.setRowCount(length + 1)

    def change_data(self, row, col):
        # Check for key format
        if col == 0 and self.tblVariables.currentItem() is not None:
            if self.tblVariables.currentItem().text() != "" and not search(
                "^[a-zA-Z_][a-zA-Z0-9_]*$",
                self.tblVariables.item(row, 0).text()
            ):
                # Re-assign old value
                self.tblVariables.setItem(
                    row, 0,
                    QTableWidgetItem(self.current_value, 0)
                )
                # Warn user about formatting
                QMessageBox.warning(
                    self, "Disallowed Format",
                    "Variables must begin with letters and can only consist of alphanumeric characters and underscores."
                )
        # Get keys as lists
        if col == 0:
            keys = []
            for row in range(self.tblVariables.rowCount()):
                keys.append(
                    self.tblVariables.item(row, 0).text()
                    if self.tblVariables.item(row, 0) is not None
                    else ""
                )
            self.keys = keys
        # Get values as lists
        else:
            values = []
            for row in range(self.tblVariables.rowCount()):
                values.append(
                    self.tblVariables.item(row, 1).text()
                    if self.tblVariables.item(row, 1) is not None
                    else ""
                )
            self.values = values

        # Update current value
        self.get_current_value(row, col)

    # Delete a variable
    def delete_variable(self):
        # Prompt for deletion
        if QMessageBox.warning(
            self, "Confirm Deletion",
            "Are you sure you want to delete this variable?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            current = self.tblVariables.currentRow()
            # Check if there is a selection
            if current > -1:
                self.keys.pop(current)
                self.values.pop(current)
                print(self.keys)
                print(self.values)
                self.reload_table()

    def save_variables(self) -> None:
        # Remove duplicates
        unique = dict(
            (key, value)
            for key, value in zip(self.keys, self.values)
            # Check if variable is valid
            if search("^[a-zA-Z_][a-zA-Z0-9_]*$", key)
        )
        # Check for duplicate values
        warn_for_nonunique = """
<p>
    Duplicated variables have been detected. The <b>last value</b> provided will be used.
</p>""" if len(list(unique.keys())) != len(self.values) else ""
        keys = unique.keys()
        values = unique.values()
        # Get valid variables
        result = ""
        warn_for_empty = ""
        for key, value in zip(keys, values):
            if all([len(key), len(value)]):
                result += f"{key}={value}\n"
            else:
                warn_for_empty = """
    <p>
        <b>Other variables will not be used due to empty fields!</b>
    </p>"""
        result = result[:-1]
        html_result = result.replace("\n", "<br />\n")
        # Set Message
        message = """<html>There are no valid variables. Do you want to write an empty /etc/environment file?</html>""" \
            if len(self.keys) < 1 \
            else f"""<html>
    <p>The following variables will be written to /etc/environments file:</p>
    <p>
        <font color="orange" face="monospace">
            {html_result}
        </font>
    </p>{warn_for_empty}{warn_for_nonunique}
    <p>Do you agree with these changes?</p>
</html>"""
        # Ask for changes
        msgAgreement = QMessageBox(self)
        msgAgreement.setTextFormat(Qt.RichText)
        agree: bool = msgAgreement.information(
            self, "Check Variables",
            message, QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Ok
        # Do changes if user agrees
        if agree:
            system(f"""echo '# This configuration file has been edited using the "make-endeavouros-great" application.

{result}' | pkexec tee /etc/environment""")
