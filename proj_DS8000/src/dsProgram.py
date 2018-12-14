import sys
import os
from PyQt5  import QtCore, QtGui, uic, QtWidgets

            
class NetworkAdapter:
    def __init__(self, netAdapt):
        self.netAdapt = netAdapt 
    
    def setNetAdapter(self):
        os.system("netsh int ip set address 13 static 192.168.100.2 255.255.255.0")
        
    def resetNetAdapter(self):
        os.system("ipconfig /release")
        os.system("ipconfig /renew")
        os.system("netsh int ip set address 13 dhcp")        

class GUIMainWindow(QtWidgets.QMainWindow):
    
   
    
        def __init__(self,app):
            super(GUIMainWindow,self).__init__()
            
            
            self.app = app
            uic.loadUi(os.getcwd() + '\DS8000.ui', self)
            self.setWindowTitle("DS8000 Programming")
            
            self.networkAdapt = NetworkAdapter(self)

        def enableConfig(self):
            self.configBox.setEnabled(True)
            self.startButton.setEnabled(False)
            
        def startConfig(self):
            self.networkAdapt.setNetAdapter()
        
        def resetConfig(self):
            self.networkAdapt.resetNetAdapter()
            
   
def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = GUIMainWindow(app)
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        import os
        print("GUI Crashed: %s\n" % e)
        
# end of class MyApp

if __name__ == "__main__":
    main()