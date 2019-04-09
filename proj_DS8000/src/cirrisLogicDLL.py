from ctypes import *
from dsProgram import *


#pacNfirmDLL = cdll.LoadLibrary(currDir + '\\pacnfirm.dll')
#papollerDLL = cdll.LoadLibrary(currDir + '\\papoller2.dll')

class PacNDisco:
    
    def __init__(self,pacNdisco): 
        self.pacNdisco = self
        self.pacNdiscoDLL = cdll.LoadLibrary(currDir + '\\pacndisco.dll')
        self.pacManager = PacManager
        
    def runIT(self):
        self.here = self.pacNdiscoDLL.show_console()
        print(self.here)
    
    
    
class PacManager(PacNDisco):
    
    def __init__(self, pacManager):
        self.pacManager = self
        self.adapterVector = {}
        
        
    def getAdapter(self,adaptName):
        self.pacAdapter = PacAdapter
        tempAdapt = adaptName
        print(tempAdapt)
        return tempAdapt
    
    def showConsole(self):
        print("diagnostics")
    
class PacAdapter(PacManager):
    
    def __init__(self, pacManager):
        PacManager.__init__(self, pacManager)
        self.pacDevice = PacDevice
        autoassign = False
        send_reservation = False
        ip = "0.0.0.0"
        ip_end = ".0"
        ip_end_default = ".0"
        ip_start = "0."
        ip_subnet = "255.255.255.0"
    
    def start(self):
        cobraDevices = ()
        if self.autoassign == True:
            for device in cobraDevices:
                if (device.ip == "0.0.0.0"):
                    print("assigning IP")
       
    def device_First(self):
        return self.cobraDevices[0]
    
    def device_Next(self,currDevice):
        tempDevice = self.cobraDevices[currDevice]
        return self.cobraDevices[tempDevice + 1]
    
    def device_Get(self,mac):
        for macDevice in self.cobraDevices:
            tempMac = macDevice.mac_address
            if tempMac == mac:
                deviceMac = self.cobraDevices[macDevice]
        return deviceMac
    
    def device_Remove(self,mac):
        removeDevice = self.device_Get(mac)
        self.cobraDevices.remove(removeDevice)
    
class PacDevice(PacAdapter):
    def __init__(self,pacDevice):
        self.pacDevice = self
        ip = "0.0.0.0"
        mac_address = ""
        age = 0 #milliseconds since last reservation
        valid = False #if actual device
        
    
        
    
        
def main():
    pac = PacNDisco(sys.argv)
    pac.runIT()


main()