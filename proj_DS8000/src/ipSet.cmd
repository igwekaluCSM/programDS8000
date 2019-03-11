@ECHO OFF
netsh int dump > currentNetConfig.dat
FOR /F "tokens=1,5*" %%P IN ('netsh int ipv4 show int ^| findstr "Local Ethernet"') DO SET idNum=%%P
netsh int ip set address %idNum% static 192.168.100.2 255.255.255.0
netsh int ip add address %idNum% 192.168.101.2 255.255.255.0
@ECHO ON	