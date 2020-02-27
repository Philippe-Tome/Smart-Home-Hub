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

        self.red_pin=12 # LEDs
        self.green_pin=16
        self.blue_pin=20
        self.push_button=15 # mechanical push button

        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)
        GPIO.setup(self.push_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.output(self.red_pin, False)
        GPIO.output(self.green_pin, False)
        GPIO.output(self.blue_pin, False)


        self.button_1_state=False
        self.button_2_state=False
        self.button_3_state=False

        self.pushButton.clicked.connect(self.toggleLight1)
        self.pushButton_2.clicked.connect(self.toggleLight2)
        self.pushButton_3.clicked.connect(self.toggleLight3)

        GPIO.add_event_detect(self.push_button,GPIO.RISING,callback=self.button_callback) 
        
        message = input("Press enter to quit\n\n") 

    def button_callback(self, channel):
        print("Button was pushed!")
        self.pushButton_4.setText("on")


    def toggleLight1(self):
        if self.button_1_state==False:
            self.button_1_state=True
            self.pushButton.setText("on")
            GPIO.output(self.red_pin, True)
        else:
            self.button_1_state=False
            self.pushButton.setText("off")
            GPIO.output(self.red_pin, False)
        print("red button pressed")

    def toggleLight2(self):
        if self.button_2_state==False:
            self.button_2_state=True
            self.pushButton_2.setText("on")
            GPIO.output(self.green_pin, True)
        else:
            self.button_2_state=False
            self.pushButton_2.setText("off")
            GPIO.output(self.green_pin, False)
        print("green button pressed")

    def toggleLight3(self):
        if self.button_3_state==False:
            self.button_3_state=True
            self.pushButton_3.setText("on")
            GPIO.output(self.blue_pin, True)
        else:
            self.button_3_state=False
            self.pushButton_3.setText("off")
            GPIO.output(self.blue_pin, False)
        print("blue button pressed")



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


