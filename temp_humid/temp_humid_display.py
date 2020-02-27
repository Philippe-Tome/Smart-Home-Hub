import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import Adafruit_DHT
from RPi import GPIO

SENSOR_MODEL = 11
GPIO.setmode(GPIO.BCM)

class SensorInterface(qtc.QObject):

    temperature = qtc.pyqtSignal(float)
    humidity = qtc.pyqtSignal(float)
    read_time = qtc.pyqtSignal(qtc.QTime)

    def __init__(self, pin, sensor_model, fahrenheit=False):
        super().__init__()
        self.pin = pin
        self.model = sensor_model
        self.fahrenheit = fahrenheit

    @qtc.pyqtSlot()
    def take_reading(self):
        h, t = Adafruit_DHT.read_retry(self.model, self.pin)
        if self.fahrenheit:
            t = ((9/5) * t) + 32
        self.temperature.emit(t)
        self.humidity.emit(h)
        self.read_time.emit(qtc.QTime.currentTime())
    
    


class MainWindow(qtw.QMainWindow):

    def __init__(self):
        """MainWindow constructor.
        
        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        widget = qtw.QWidget()
        widget.setLayout(qtw.QFormLayout())
        self.setCentralWidget(widget)
        p = widget.palette()
        p.setColor(qtg.QPalette.WindowText, qtg.QColor('cyan'))
        p.setColor(qtg.QPalette.Window, qtg.QColor('navy'))
        p.setColor(qtg.QPalette.Button, qtg.QColor('#335'))
        p.setColor(qtg.QPalette.ButtonText, qtg.QColor('cyan'))
        self.setPalette(p)
        tempview = qtw.QLCDNumber()
        humview = qtw.QLCDNumber()
        tempview.setSegmentStyle(qtw.QLCDNumber.Flat)
        humview.setSegmentStyle(qtw.QLCDNumber.Flat)
        widget.layout().addRow('Temperature', tempview)
        widget.layout().addRow('Humidity', humview)
        self.sensor = SensorInterface(4, SENSOR_MODEL, False)
        self.sensor_thread = qtc.QThread()
        self.sensor.moveToThread(self.sensor_thread)
        self.sensor_thread.start()
        self.sensor.temperature.connect(tempview.display)
        self.sensor.humidity.connect(humview.display)
        self.sensor.read_time.connect(self.show_time)
        def show_time(self, qtime):
            self.statusBar().showMessage(
                f'Read at {qtime.toString("HH:mm:ss")}')
        self.timer = qtc.QTimer(interval=(60000))
        self.timer.timeout.connect(self.sensor.take_reading)
        self.timer.start()
        readbutton = qtw.QPushButton('Read Now')
        widget.layout().addRow(readbutton)
        readbutton.clicked.connect(self.sensor.take_reading)
        
        # End main UI code
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())
