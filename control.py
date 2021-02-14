from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from caclulator_Maksim_Derkach import Ui_Calculator
app = QtWidgets.QApplication(sys.argv)
Calculator = QtWidgets.QDialog()
ui = Ui_Calculator()
ui.setupUi(Calculator)
Calculator.show()

def action_plus():
    text = ui.label_output.text()
    ui.label_output.setText(text + "+")
def action_minus():
    text = ui.label_output.text()
    ui.label_output.setText(text + "-")
def action_equals():
    text = ui.label_output.text()
    ui.label_output.setText(text + "=")
def action_divide():
    text = ui.label_output.text()
    ui.label_output.setText(text + "/")
def action_multiply():
    text = ui.label_output.text()
    ui.label_output.setText(text + "X")
def pushbutton_one():
    text = ui.label_output.text()
    ui.label_output.setText(text + "1")
def pushbutton_two():
    text = ui.label_output.text()
    ui.label_output.setText(text + "2")
def pushbutton_three():
    text = ui.label_output.text()
    ui.label_output.setText(text + "3")
def pushbutton_four():
    text = ui.label_output.text()
    ui.label_output.setText(text + "4")
def pushbutton_five():
    text = ui.label_output.text()
    ui.label_output.setText(text + "5")
def pushbutton_six():
    text = ui.label_output.text()
    ui.label_output.setText(text + "6")
def pushbutton_seven():
    text = ui.label_output.text()
    ui.label_output.setText(text + "7")
def pushbutton_eight():
    text = ui.label_output.text()
    ui.label_output.setText(text + "8")
def pushbutton_nine():
    text = ui.label_output.text()
    ui.label_output.setText(text + "9")
def pushbutton_zero():
    text = ui.label_output.text()
    ui.label_output.setText(text + "0")
ui.pushButton_plus.clicked.connect(action_plus)
ui.pushButton_minus.clicked.connect(action_minus)
ui.pushButton_equals.clicked.connect(action_equals)
ui.pushButton_divided.clicked.connect(action_divide)
ui.pushButton_multiply.clicked.connect(action_multiply)
ui.pushButton_one.clicked.connect(pushbutton_one)
ui.pushButton_two.clicked.connect(pushbutton_two)
ui.pushButton_three.clicked.connect(pushbutton_three)
ui.pushButton_four.clicked.connect(pushbutton_four)
ui.pushButton_five.clicked.connect(pushbutton_five)
ui.pushButton_six.clicked.connect(pushbutton_six)
ui.pushButton_seven.clicked.connect(pushbutton_seven)
ui.pushButton_eight.clicked.connect(pushbutton_eight)
ui.pushButton_nine.clicked.connect(pushbutton_nine)
ui.pushButton_zero.clicked.connect(pushbutton_zero)
sys.exit(app.exec_())