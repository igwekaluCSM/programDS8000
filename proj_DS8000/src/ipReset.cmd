@ECHO OFF
netsh exec currentNetConfig.dat
ipconfig /renew
Ncpa.cpl, not Netcpl.cpl
ECHO Right Click 'Local Area Connection' and select 'Properties
PAUSE
ECHO In the list select 'Internet Protocol Version 4 (TCP/IPv4) and click 'Properties'
PAUSE 
ECHO Select 'Obtain an IP Address automatically' and click OK
PAUSE
ECHO Close the windows...
PAUSE
@ECHO ON