import sys
import os
import time 
from PyQt5  import QtCore, QtGui, uic, QtWidgets
from asyncio.tasks import wait

currDir  = os.getcwd()
            
class NetworkAdapter:
    def __init__(self, netAdapt):
        self.netAdapt = netAdapt 
        
    def setNetAdapter(self):
        
        #os.system(".\netSet.cmd")
        
        os.system( currDir + "\\netSet.cmd >>netsetOutput.txt")
        #os.system( currDir + "\\ipSet.cmd >> ipsetOutput.txt")
        
        '''
        os.system("FOR /F \"tokens=4\" %G IN ('netsh int show int ^|find \"Local\"') DO SET netName=%G")
        os.system("FOR /F \"tokens=4\" %G IN ('netsh int show int ^|find \"Ethernet\"') DO echo Result is [%G]")
        #os.system("SET netName=%G%")
        os.system("ECHO %G")
        os.system("netsh int set int ECHO %netName% enable")
        #os.system("netsh int set int \"Ethernet\" enable")
        '''
        #except:
        #   print("Already Enabled")
 
    def resetNetAdapter(self):
    
        #os.system("netsh int ip set address 13 dhcp")
        os.system( currDir + "\\ipReset.cmd >> resetOutput.txt")
        
class GUIMainWindow(QtWidgets.QMainWindow):
    
   
    
        def __init__(self,app):
            super(GUIMainWindow,self).__init__()
            self.gui = self
            
            self.app = app
            uic.loadUi(os.getcwd() + '\DS8000.ui', self)
            self.setWindowTitle("DS8000 Programming")
            
            self.networkAdapt = NetworkAdapter(self)

        def enableConfig(self):
            self.configBox.setEnabled(True)
            self.startButton.setEnabled(False)
            
        def startConfig(self):
            self.networkAdapt.setNetAdapter()
            #self.fillOutput()
        def resetConfig(self):
            self.networkAdapt.resetNetAdapter()
            
        
        def fillOutput(self):
            outputFile = open(currDir + "\\ipsetOutput.txt")
            setLines = outputFile.readlines()
            outputFile.close()
            for line in setLines:
                self.consoleOutput.setText(line)
        
        
   
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