from ctypes import *
from dsProgram import *


#pacNfirmDLL = cdll.LoadLibrary(currDir + '\\pacnfirm.dll')
#papollerDLL = cdll.LoadLibrary(currDir + '\\papoller2.dll')

class PacNDisco:
    
    def __init__(self,pacNdisco): 
        self.pacNdisco = self
        self.pacNdiscoDLL = cdll.LoadLibrary(currDir + '\\pacndisco.dll')
        
    def runIT(self):
        self.here = self.pacNdiscoDLL.show_console()
        print(self.here)
        
def main():
    pac = PacNDisco(sys.argv)
    pac.runIT()
    

main()