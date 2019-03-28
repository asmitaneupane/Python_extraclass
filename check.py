import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QComboBox, QDialogButtonBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 status bar example - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

class Dialog(QDialog):
    def slot_method(self):
        print('slot method is called.')

    def __init__(self):
        super(Dialog, self).__init__()

        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100,70)
        button = QPushButton("click")
        button.clicked.connect(self.slot_method)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    print ex.Dialog.QDialog()
    sys.exit(app.exec_())