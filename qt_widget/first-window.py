from PyQt4 import QtCore, QtGui, uic
import sys
class MyWidget(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = uic.loadUi('mainwindow.ui', self)
        self.ui.setWindowTitle("Hello World !!!")
        self.ui.show()
        self.connect(self.ui.btnShowMessage, QtCore.SIGNAL("clicked()"), self.DisplayMessage)

    def DisplayMessage(self):
        self.ui.lblMessage.setText("Jay Shri Ram")

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    
    t = MyWidget()
    sys.exit(app.exec_())
