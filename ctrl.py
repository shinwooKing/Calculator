class Control:
    def __init__(self,view):
        self.view = view
        self.connectSignals()

    def calculate(self):
        num1 = float(self.view.le1.text())
        num1 = float(self.view.le2.text())
        operator = self.view.cb.currentText()

        if operator == '+':
            return f'{num1} + {num2} = {self.sum(num,num2)}'
        else:
            return 'Calculator Error'

    def connectSignals(self):
        self.view.btn1.clicked.connect(lambda:
                                       self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self,a,b):
        try:
            return str(a-b)
        except:
            return 'Calculation Error'