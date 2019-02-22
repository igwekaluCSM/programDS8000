import sys
import os
import time as t
import openpyxl as op
from openpyxl import load_workbook  
from PyQt5  import QtCore, QtGui, uic, QtWidgets
from asyncio.tasks import wait
from fileinput import filename
from distutils.command.upload import upload
from PyQt5.QtWidgets import QFileDialog


#initialization necessities
currDir  = os.getcwd()
os.system(currDir + "\\pythonInstall.cmd")

class BPLPrinter:
    def __init__(self, excDat):
        self.excDat= excDat
    
    def changeBPLDirectory(self):
        for bplText in open(currDir + '\\BPL.xml', 'r'):
            if "insert_directory_here" in bplText:
                bplText=bplText.replace("insert_directory_here" , currDir + '/BPL.xsd')
                bplText=bplText.replace('\\','/')
                print(bplText)
                        
class ExcelData:
    def __init__(self, excDat):
        self.excDat= excDat
    
    def createExcel(self):

        os.system(currDir  + '\\excelDS8000.xlsm')
        self.openSheet()
        print('range: ' + self.labelRange['B20'].value)
    
    def openSheet(self):
        
        self.excelSheet = op.Workbook()
        self.excelSheet = load_workbook(filename = currDir  + '\\excelDS8000.xlsm')
        self.labelRange = self.excelSheet['Sheet1']
    
    def loadSheet(self,fileLocation):
        self.excelSheet = op.Workbook()
        self.excelSheet = load_workbook(filename = fileLocation)
        self.labelRange = self.excelSheet['Sheet1']
        try:
            self.gatherLabels(self.labelRange)
        except Exception as e:
            import os
            print("GUI Crashed: %s\n" % e)          
    
    def gatherLabels(self,labelImport):
        x = "7"
        label = labelImport["B"+ x]
        while label  != "":
            currLabel = "B" + x
            print(self.labelRange[currLabel].value)
            x = int(x)
            x+=1
            x = str(x)
            
class NetworkAdapter:
    def __init__(self, gui):
        self.gui =  gui 
        
    def setNetAdapter(self):
        
        #os.system(".\netSet.cmd")
        self.gui.resetNetAdaptButton.setEnabled(True)
        self.gui.setIPAdaptButton.setEnabled(False)
        self.gui.skipNetButton.setEnabled(False)
        self.gui.newExcelButton.setEnabled(True)
        self.gui.uploadExcelButton.setEnabled(True)
        #os.system( currDir + "\\netSet.cmd >> netsetOutput.txt")
        os.system( currDir + "\\ipSet.cmd >> ipsetOutput.txt")
        
        '''
        os.system("FOR /F \"tokens=4\" %G IN ('netsh int show int ^|find \"Local\"') DO SET netName=%G")
        os.system("FOR /F \"tokens=4\" %G IN ('netsh int show int ^|find \"Ethernet\"') DO echo Result is [%G]")
        #os.system("SET netName=%G%")
        os.system("ECHO %G")
        os.system("netsh int set int ECHO %netName% enable")
        #os.system("netsh int set int \"Ethernet\" enable")
        '''
        
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
        self.fillOutput("\\ipsetOutput.txt")
    def resetConfig(self):
        self.networkAdapt.resetNetAdapter()
        self.fillOutput("\\resetNet.txt")
    def skipConfig(self):
        self.networkAdapt.skipNetSet()
        
    def newExcel(self):
        self.excDat.createExcel()
        
    def fillOutput(self, fileName):
        outputFile = open(currDir + fileName)
        setLines = outputFile.readlines()
        outputFile.close()
        try:
            for line in setLines:
                self.consoleOutput.append(line)
        except Exception as e:  
            import os
            print("GUI Crashed: %s\n" % e)
        
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
        
        self.excDat = ExcelData(self)
        uic.loadUi(currDir + '\\uploadWindow.ui', self)
        
          
    def openBrowse(self):
        self.browseWindow = QtWidgets.QFileDialog
        self.browseDirectory = self.browseWindow.getOpenFileName()
        self.showDirectory()
        #print(self.browseDirectory[0])
        
    def showDirectory(self):
        try:
            self.directoryOutput.setText(self.browseDirectory[0])
        except Exception as e:  
            import os
            print("GUI Crashed: %s\n" % e)
        
        
    def uploadData(self):
        
        self.excDat.loadSheet(self.browseDirectory[0])
        
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