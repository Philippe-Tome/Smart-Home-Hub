#!/usr/bin/python3
from main_window import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#led pin red=12, green=16, blue=20

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent) # append our ui code to the rest of this class
        self.setupUi(self)  # setting all the Ui up

        self.red_led=12
        self.green_pin=16
        self.blue_pin=20
        # self.button_pin=20

        # GPIO.setup(self.button_pin, GPIO.IN)
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)
        GPIO.output(self.red_pin, False)
        GPIO.output(self.green_pin, False)
        GPIO.output(self.blue_pin, False)


        self.button_1_state=False
        self.button_2_state=False
        self.button_3_state=False
        self.pushButton.clicked.connect(self.toggleLight)
        self.pushButton_2.clicked.connect(self.toggleLight)
        self.pushButton_3.clicked.connect(self.toggleLight)


    def toggleLight(self):
        if self.button_state==False:
            self.button_state=True
            self.pushButton.setText("on")
            GPIO.output(self.led_pin, True)
        else:
            self.button_state=False
            self.pushButton.setText("off")

            GPIO.output(self.led_pin, False)
        print("push button pressed")


# button 
# google Qthread
#google prevent screen to fall asleep


def main():
    app = QtWidgets.QApplication(sys.argv)
    form=App()
    form.show()
    #form.showFullScreen()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


