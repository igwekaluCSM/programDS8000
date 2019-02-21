@ECHO OFF
netsh exec currentNetConfig.dat
ipconfig /renew
Ncpa.cpl, not Netcpl.cpl
ECHO Right Click 'Local Area Connection' and select 'Properties
ECHO In the list select 'Internet Protocol Version 4 (TCP/IPv4) and click 'Properties' 
ECHO Select 'Obtain an IP Address automatically' and click OK
ECHO Close the windows...
@ECHO ON