@ECHO OFF
netsh int dump > currentNetConfig.dat
FOR /F "tokens=1,5*" %%P IN ('netsh int ipv4 show int ^| findstr "Local Ethernet"') DO SET idName=%%P
netsh int ip set address %idName% static 192.168.100.2 255.255.255.0
netsh int ip add address %idName% 192.168.101.2 255.255.255.0
@ECHO ON	