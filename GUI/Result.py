from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout


class ResultWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create widgets
        self.lblStatusCode = QLabel(self)
        self.lblStatus = QLabel(self)
        self.lblStatus.setWordWrap(True)

        # Insert widgets to layout
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.lblStatusCode)
        self.layout.addWidget(self.lblStatus, 1)

    def setStatus(self, statusCode):
        self.lblStatusCode.setText(f"Exited({statusCode}):")
        if statusCode == 0:
            self.lblStatus.setText("Operation successfull.")
            self.lblStatusCode.setStyleSheet("color: green")
        elif statusCode == -1:
            self.lblStatus.setText("Terminal closed by user.")
            self.lblStatusCode.setStyleSheet("color: gray")
        else:
            self.lblStatus.setText("Opeation failed.")
            self.lblStatusCode.setStyleSheet("color: red")
