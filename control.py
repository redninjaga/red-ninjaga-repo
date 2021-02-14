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
    ui.label_output.setText(text+"+")
def pushbutton_one():
    text = ui.label_output.text()
    ui.label_output.setText(text + "1")

ui.pushButton_plus.clicked.connect(action_plus)
ui.pushButton_one.clicked.connect(pushbutton_one)


sys.exit(app.exec_())