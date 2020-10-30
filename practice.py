import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.setVariables()
        self.keypad()
        self.show()
    
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        #buttons
        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton("Enter", clicked = self.evaluate)
        btn_clear  = qtw.QPushButton("Clear", clicked = self.clear)
        btn_plus   = qtw.QPushButton("+", clicked = lambda: self.key_press("+"))
        btn_minus  = qtw.QPushButton("-", clicked = lambda: self.key_press("-"))
        btn_mul    = qtw.QPushButton("*", clicked = lambda: self.key_press("*"))
        btn_div    = qtw.QPushButton("/", clicked = lambda: self.key_press("/"))
        btn9       = qtw.QPushButton("9", clicked = lambda: self.num_press("9"))
        btn8       = qtw.QPushButton("8", clicked = lambda: self.num_press("8"))
        btn6       = qtw.QPushButton("7", clicked = lambda: self.num_press("7"))
        btn7       = qtw.QPushButton("6", clicked = lambda: self.num_press("6"))
        btn5       = qtw.QPushButton("5", clicked = lambda: self.num_press("5"))
        btn4       = qtw.QPushButton("4", clicked = lambda: self.num_press("4"))
        btn3       = qtw.QPushButton("3", clicked = lambda: self.num_press("3"))
        btn2       = qtw.QPushButton("2", clicked = lambda: self.num_press("2"))
        btn1       = qtw.QPushButton("1", clicked = lambda: self.num_press("1"))
        btn0       = qtw.QPushButton("0", clicked = lambda: self.num_press("0"))

        container.layout().addWidget(self.result_field, 0, 0, 1, 4)
        container.layout().addWidget(btn_result, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)
        container.layout().addWidget(btn9, 2, 0)
        container.layout().addWidget(btn8, 2, 1)
        container.layout().addWidget(btn7, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn6, 3, 0)
        container.layout().addWidget(btn5, 3, 1)
        container.layout().addWidget(btn4, 3, 2)
        container.layout().addWidget(btn_minus, 3, 3)
        container.layout().addWidget(btn3, 4, 0)
        container.layout().addWidget(btn2, 4, 1)
        container.layout().addWidget(btn1, 4, 2)
        container.layout().addWidget(btn_mul, 4, 3)
        container.layout().addWidget(btn0, 5, 0, 1, 3)
        container.layout().addWidget(btn_div, 5, 3)

        self.layout().addWidget(container)

    def setVariables(self):
        self.stringOperation = ""
        self.opeartors = ['+', '-', '/', '*']

    def num_press(self, num):
        if len(self.stringOperation) == 0 and num == '0':
            return
        if len(self.stringOperation) != 0 and self.stringOperation[-1] == '0' and num == '0':
            return
        self.stringOperation += num
        self.result_field.setText(self.stringOperation)

    def key_press(self, key):
        if len(self.stringOperation) == 0:
            return
        if self.stringOperation[-1] in self.opeartors:
            return
        self.stringOperation += key
        self.result_field.setText(self.stringOperation)

    def clear(self):
        self.stringOperation = self.stringOperation[:-1]
        self.result_field.setText(self.stringOperation)

    def evaluate(self):
        if self.stringOperation[-1] in self.opeartors:
            return

        # calculation of the answer
        result = eval(self.stringOperation)
        self.result_field.setText(str(result))





app = qtw.QApplication([])

window = MainWindow()

app.exec_()