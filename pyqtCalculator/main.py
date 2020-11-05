import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit


# Creating window (main Widget)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("Name: ")
        name_input = QLineEdit()
        button = QPushButton("Set Name")

        h = QHBoxLayout()
        # h.addStretch(1)
        h.addWidget(label)
        h.addWidget(name_input)

        v = QVBoxLayout()
        # v.addStretch(1)
        v.addLayout(h)
        v.addWidget(button)

        self.setLayout(v)

        self.setWindowTitle("Horizontal Layout")
        self.show()


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