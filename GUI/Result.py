from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout


class ResultWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create widgets
        self.lblStatusCode = QLabel("Hasn't Run.", self)
        self.lblStatus = QLabel("No Process.", self)

        # Insert widgets to layout
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.lblStatusCode)
        self.layout.addWidget(self.lblStatus, 1)
        print(self.lblStatus.text())

    def setStatus(self, statusCode):
        self.lblStatusCode.setText(f"Exited({statusCode}):")
        if statusCode == 0:
            self.lblStatus.setText("Operation successfull.")
            self.lblStatusCode.setStyleSheet("color: green")
        else:
            self.lblStatus.setText("Opeation failed.")
            self.lblStatusCode.setStyleSheet("color: red")
