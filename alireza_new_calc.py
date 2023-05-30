from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QApplication
import sys
from sympy import *
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # تنظیم عنوان برای پنجره
        self.setWindowTitle("ماشین حساب")
        
        # تعریف یک widget اصلی برای پنجره
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # تعریف یک layout برای قرار دادن دکمه ها و نتیجه
        grid_layout = QGridLayout()
        
        # تعریف یک LineEdit برای صفحه نمایش نتیجه
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True) # تعیین خواندنی بودن نمایش نتیجه
        
        # اضافه کردن دکمه ها به layout
        # از تابع lambda برای اتصال دکمه ها به توابع استفاده می کنیم.
        # تابع lambda، قابلیت ارسال پارامتر ندارد. بنابراین، 
        # برای ارسال پارامتر به تابع، از partial استفاده می کنیم.
        btn_1 = QPushButton('1', self)
        btn_1.clicked.connect(lambda: self.numberPressed(1))
        grid_layout.addWidget(btn_1, 1, 0)

        btn_2 = QPushButton('2', self)
        btn_2.clicked.connect(lambda: self.numberPressed(2))
        grid_layout.addWidget(btn_2, 1, 1)

        btn_3 = QPushButton('3', self)
        btn_3.clicked.connect(lambda: self.numberPressed(3))
        grid_layout.addWidget(btn_3, 1, 2)

        btn_4 = QPushButton('4', self)
        btn_4.clicked.connect(lambda: self.numberPressed(4))
        grid_layout.addWidget(btn_4, 2, 0)

        btn_5 = QPushButton('5', self)
        btn_5.clicked.connect(lambda: self.numberPressed(5))
        grid_layout.addWidget(btn_5, 2, 1)

        btn_6 = QPushButton('6', self)
        btn_6.clicked.connect(lambda: self.numberPressed(6))
        grid_layout.addWidget(btn_6, 2, 2)

        btn_7 = QPushButton('7', self)
        btn_7.clicked.connect(lambda: self.numberPressed(7))
        grid_layout.addWidget(btn_7, 3, 0)

        btn_8 = QPushButton('8', self)
        btn_8.clicked.connect(lambda: self.numberPressed(8))
        grid_layout.addWidget(btn_8, 3, 1)

        btn_9 = QPushButton('9', self)
        btn_9.clicked.connect(lambda: self.numberPressed(9))
        grid_layout.addWidget(btn_9, 3, 2)

        btn_0 = QPushButton('0', self)
        btn_0.clicked.connect(lambda: self.numberPressed(0))
        grid_layout.addWidget(btn_0, 4, 1)

        btn_plus = QPushButton('+', self)
        btn_plus.clicked.connect(lambda: self.oper('+'))
        btn_plus.setStyleSheet("background-color: Purple")
        grid_layout.addWidget(btn_plus, 4, 3)

        btn_minus = QPushButton('-', self)
        btn_minus.clicked.connect(lambda: self.oper('-'))
        btn_minus.setStyleSheet("background-color: Pink")
        grid_layout.addWidget(btn_minus, 1, 3)

        btn_multiply = QPushButton('*', self)
        btn_multiply.clicked.connect(lambda: self.oper('*'))
        btn_multiply.setStyleSheet("background-color: Green")
        grid_layout.addWidget(btn_multiply, 2, 3)

        btn_divide = QPushButton('/', self)
        btn_divide.clicked.connect(lambda: self.oper('/'))
        btn_divide.setStyleSheet("background-color: Yellow")
        grid_layout.addWidget(btn_divide, 3, 3)

        btn_c = QPushButton('c', self)
        btn_c.clicked.connect(self.btn_clear)
        btn_c.setStyleSheet("background-color: Orange")
        grid_layout.addWidget(btn_c, 4, 0)

        btn_c_back = QPushButton('back', self)
        btn_c_back.clicked.connect(self.btn_c_back)
        btn_c_back.setStyleSheet("background-color: red")
        grid_layout.addWidget(btn_c_back, 0, 3)


        btn_equals = QPushButton('=', self)
        btn_equals.clicked.connect(self.calc)
        grid_layout.addWidget(btn_equals, 4, 2)

        # قرار دادن LineEdit و دکمه ها در layout
        grid_layout.addWidget(self.result_display, -0, 0, 1, 3)
        
        # تعیین layout برای widget اصلی
        main_widget.setLayout(grid_layout)
        
    def numberPressed(self, num):
        current_text = self.result_display.text()
        self.result_display.setText(current_text + str(num))


    def btn_clear(self):
        btn_clear_a = self.result_display.text()
        self.result_display.setText(btn_clear_a [:-10000])
        # self.result_display.setText("")

    def btn_c_back(self):
        btn_clear_c = self.result_display.text()
        self.result_display.setText(btn_clear_c [:-1])
        # self.result_display.setText("")


    def oper(self, operation):
        current_text = self.result_display.text()
        try:
            if current_text[-1] in ['+', '-', '*', '/']:
                self.result_display.setText(current_text[:-1] + operation)
            else:
                self.result_display.setText(current_text + operation)
        except:
            self.result_display.setText("error")
    


    def calc(self):
        current_text = self.result_display.text()
        try:  
            if current_text == "":
                self.result_display.setText("0")
            else:
                current_text = self.result_display.text()
                expr = sympify(current_text)
                result = simplify(expr)
                self.result_display.setText(str(result))
        except:
            self.result_display.setText("error")    




if __name__ == "__main__": 
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
