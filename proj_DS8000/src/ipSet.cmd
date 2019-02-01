@ECHO OFF
netsh int dump > currentNetConfig.dat
netsh int ip set address 13 static 192.168.100.2 255.255.255.0
netsh int ip add address 13 192.168.101.2 255.255.255.0
@ECHO ON	