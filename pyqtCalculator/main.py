import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text # so we can refrence it later
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, value):
        if value == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif value == "AC":
            self.results.setText("")
        else:
            current_value = self.results.text()
            new_value = current_value + str(value)
            self.results.setText(new_value)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Calculator")
        self.CreateApp()

    def CreateApp(self):

        # Creating a variable named Grid
        grid = QGridLayout()
        results = QLineEdit()

        buttons = ["AC", "C", "CE", "/",
                    7, 8, 9, "*",
                    4, 5, 6, "-",
                    1, 2, 3, "+",
                    0, ".", "="]

        grid.addWidget(results, 0, 0, 1, 4)

        row = 1
        column = 0

        for button in buttons:
            if column > 3:
                column = 0
                row += 1

            buttonObj = Button(button, results)

            if button == 0:
                grid.addWidget(buttonObj.b, row, column, 1, 2)
                column += 1
            else:
                grid.addWidget(buttonObj.b, row, column, 1, 1)

            column += 1

        self.setLayout(grid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())





    '''
    button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Last")

        grid.addWidget(button1, 0, 0, 1, 1) # the first param is the object then row, column, row, column. So, here the button is in the first row and first column, then how many rows its going to occupy - spacing -
        grid.addWidget(button2, 0, 1, 1, 1)
        grid.addWidget(button3, 0, 2, 1, 1)
        grid.addWidget(button4, 1, 0, 1, 2)
    '''