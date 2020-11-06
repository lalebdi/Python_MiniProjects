import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit


# Creating window (main Widget)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):
        self.text_label = QLabel("There has been no name entered, so I can't do anything yet.")
        self.label = QLabel("Name: ")
        self.name_input = QLineEdit()
        self.button = QPushButton("Clicked: 0")

        self.button.setText("Set Name")
        self.button.clicked.connect(self.alterName)
        h = QHBoxLayout()
        # h.addStretch(1)
        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addWidget(self.text_label)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)

        self.setWindowTitle("Nothing clicked")
        self.show()

    def alterName(self):
        inputted_text = self.name_input.text()
        our_string = "You've entered" + inputted_text
        self.text_label.setText(our_string)
        self.setWindowTitle((inputted_text + "'s Window"))



if __name__ == "__main__": # to run the script
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())



'''
initial layout
 label = QLabel("Hi, this is the label")
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        horizontal = QHBoxLayout()
        horizontal.addStretch()

        horizontal.addWidget(okButton)
        horizontal.addWidget(cancelButton)

        vertical = QVBoxLayout()
        vertical.addWidget(label)
        vertical.addStretch(1)
        vertical.addLayout(horizontal)

        self.setLayout(vertical)

'''