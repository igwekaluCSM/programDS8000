import sys
import os
import time as t
import openpyxl as op
from openpyxl import load_workbook  
from PyQt5  import QtCore, QtGui, uic, QtWidgets
from asyncio.tasks import wait
from fileinput import filename
from distutils.command.upload import upload

currDir  = os.getcwd()

for bplText in open(currDir + '\\BPL.xml', 'r'):
    if "insert_directory_here" in bplText:
        bplText=bplText.replace("insert_directory_here" , currDir + '/BPL.xsd')
        bplText=bplText.replace('\\','/')
        print(bplText)
os.system(currDir + "\\pythonInstall.cmd")

class ExcelData:
    def __init__(self, excDat):
        self.excDat= excDat
    
    def createExcel(self):

        os.system(currDir  + '\\excelDS8000.xlsm')
        self.openSheet()
        print('range: ' + self.labelRange['B7'].value)
    
    def openSheet(self):
        
        self.excelSheet = op.Workbook()
        self.excelSheet = load_workbook(filename = currDir  + '\\excelDS8000.xlsm')
        self.labelRange = self.excelSheet['Sheet1']
        
        
class NetworkAdapter:
    def __init__(self, gui):
        self.gui =  gui 
        
    def setNetAdapter(self):
        
        #os.system(".\netSet.cmd")
        self.gui.resetNetAdaptButton.setEnabled(True)
        self.gui.setIPAdaptButton.setEnabled(False)
        #os.system( currDir + "\\netSet.cmd >>netsetOutput.txt")
        os.system( currDir + "\\ipSet.cmd >> ipsetOutput.txt")
        
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
        self.gui.resetNetAdaptButton.setEnabled(False)
        self.gui.setIPAdaptButton.setEnabled(True)
        
        #os.system("netsh int ip set address 13 dhcp")
        os.system( currDir + "\\ipReset.cmd >> resetOutput.txt")
        
    def skipNetSet(self):
        
        self.gui.resetNetAdaptButton.setEnabled(True)
        self.gui.setIPAdaptButton.setEnabled(False)
        self.gui.newExcelButton.setEnabled(True)
        self.gui.uploadExcelButton.setEnabled(True)
        self.gui.skipNetButton.setEnabled(False)
        
        
class GUIMainWindow(QtWidgets.QMainWindow):
    
    def __init__(self,app):
        super(GUIMainWindow,self).__init__()
        self.gui = self
        
        self.app = app
        uic.loadUi(currDir + '\DS8000.ui', self)
        self.setWindowTitle("DS8000 Programming")
        
        self.networkAdapt = NetworkAdapter(self)
        self.excDat = ExcelData(self)

    def enableConfig(self):
        self.setIPAdaptButton.setEnabled(True)
        self.startButton.setEnabled(False)
        self.skipNetButton.setEnabled(True)
        
    def startConfig(self):
        self.networkAdapt.setNetAdapter()
        self.fillOutput()
    def resetConfig(self):
        self.networkAdapt.resetNetAdapter()
        
    def skipConfig(self):
        self.networkAdapt.skipNetSet()
        
    def newExcel(self):
        self.excDat.createExcel()
        
    def fillOutput(self):
        outputFile = open(currDir + "\\ipsetOutput.txt")
        setLines = outputFile.readlines()
        outputFile.close()
        for line in setLines:
            self.consoleOutput.setText(line)
    
    def openUpload(self):
        try:
            self.upload= UploadWindow(self)
            self.upload.show()
            
        except Exception as e:  
            import os
            print("GUI Crashed: %s\n" % e)
        
        
class UploadWindow(QtWidgets.QDialog):
    
    def __init__(self,parent=None):
        super(UploadWindow,self).__init__(parent)
        self.gui = self
        
        uic.loadUi(currDir + '\\uploadWindow.ui', self)
        
        
        
    def openBrowse(self):
        self.browseWindow = QtWidgets.QFileDialog
        self.browseWindow.setVisible(True)
        
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