@ECHO OFF
netsh exec currentNetConfig.dat
ipconfig /renew
Ncpa.cpl, not Netcpl.cpl
@ECHO ON