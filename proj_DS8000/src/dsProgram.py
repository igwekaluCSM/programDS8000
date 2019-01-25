import sys
import os
import time
from PyQt5  import QtCore, QtGui, uic, QtWidgets
from asyncio.tasks import wait

            
class NetworkAdapter:
    def __init__(self, netAdapt):
        self.netAdapt = netAdapt 
    
    def setNetAdapter(self):
        try:
            #os.system(".\netSet.cmd")
            currDir  = os.getcwd()
            os.system(currDir + "\\netSet.cmd")
            '''
            os.system("FOR /F \"tokens=4\" %G IN ('netsh int show int ^|find \"Local\"') DO SET netName=%G")
            os.system("FOR /F \"tokens=4\" %G IN ('netsh int show int ^|find \"Ethernet\"') DO echo Result is [%G]")
            #os.system("SET netName=%G%")
            os.system("ECHO %G")
            os.system("netsh int set int ECHO %netName% enable")
            #os.system("netsh int set int \"Ethernet\" enable")
            '''
        except:
            print("Already Enabled")
        '''
        try:   
            os.system("netsh int dump > currentNetConfig.dat")
            time.sleep(1)
        except:
            print("Config File already created")
        
        try:
            os.system("ipconfig /release")
            time.sleep(1)
        except:
            print("release failed")
            
        try:
            os.system("netsh int ip set address 13 static 192.168.100.2 255.255.255.0")
            os.system("netsh int ip add address 13 192.168.101.2 255.255.255.0")
        except:
            print("set adresses failed")
        '''    
    def resetNetAdapter(self):
    
        #os.system("netsh int ip set address 13 dhcp")
        try:
            os.system("netsh exec currentNetConfig.dat")
        except:
            print("resetting network settings failed")
        try:    
            os.system("ipconfig /renew")
        except:
            print("renew failed")
        
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