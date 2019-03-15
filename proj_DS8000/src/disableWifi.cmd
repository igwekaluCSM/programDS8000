@ECHO OFF 

GOTO :firstSearch || GOTO :secondSearch || GOTO :EOF1

:firstSearch
	FOR /F "tokens=4*" %%N IN ('netsh int show int^| findstr "Wireless Wi-Fi"') DO (
		SETX wifiName '"%%N %%O"' & ECHO Network Adapter Name: %wifiName% & netsh int set int "%wifiName%" admin=DISABLED
		IF %ERRORLEVEL% EQU 0 ( 
			ECHO Wireless Network Cards Disabled & GOTO :EOF2
		) ELSE ( 
			ECHO Couldn't Disable Network Adapter Card
		)
	)
::End

:secondSearch
	FOR /F "tokens=1,5*" %%P IN ('netsh int ipv4 show int ^| findstr "Wireless Wi-Fi"') DO (
		SETX wiIdName %%P &  ECHO Network Adapter ID Number: %wiIdName% & netsh int set int "%wiIdName%" admin=DISABLED
		IF %ERRORLEVEL% EQU 0 ( 
			ECHO Wireless Network IPv4 Disabled & GOTO :EOF2
		) ELSE ( 
			ECHO Couldn't Disable Network IPv4 Card) 
		)
::End

:EOF1
	ECHO Could Not Disable Network Adapters....Manually Disable Wireless Adapters.
	GOTO :EOF
	
:EOF2
	ECHO Wireless Adapters Disabled
	GOTO :EOF
	
:EOF
ECHO ON