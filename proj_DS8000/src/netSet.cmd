:: This batch file is intended to intepret the computer specific Ethernet Adpater name.
:: test of batch comments

@ECHO OFF
::FOR /F "tokens=4" %%N IN ('netsh int show int ^| findstr "Local Ethernet"') DO SET netName=%%N %%O
FOR /F "tokens=4,*" %%N IN ('netsh int show int^| findstr "Local Ethernet"') DO SET netName="%%N %%O"
ECHO %netName%
netsh int set int ECHO %netName% admin=enabled