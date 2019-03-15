:: This batch file is intended to intepret the computer specific Ethernet Adpater name.
:: The script will enable all Ethernet connections and disable Wi-Fi connections 

@ECHO OFF 

GOTO :firstSearch || GOTO :secondSearch || GOTO :EOF1

:firstSearch
	FOR /F "tokens=4*" %%N IN ('netsh int show int^| findstr "Local Ethernet"') DO (
		setx /m netName '"%%N %%O"' & ECHO Network Adapter Name: %netName% & netsh int set int name=%netName% admin=ENABLED
		IF %ERRORLEVEL% EQU 0 ( 
			ECHO Network Card Enabled & GOTO :EOF2
		) ELSE ( 
			ECHO Couldn't Enable Network Adapter Card
		)
	)
::End
	
:secondSearch
	FOR /F "tokens=1,5*" %%P IN ('netsh int ipv4 show int ^| findstr "Local Ethernet"') DO (
		setx /m idName %%P & ECHO Network Adapter ID Number: %idName% & netsh int set int name=%idName% admin=ENABLED
		IF %ERRORLEVEL% EQU 0 ( 
			ECHO Network IPv4 Enabled & GOTO :EOF2
		) ELSE ( 
			ECHO Couldn't Enable Network IPv4 Card) 
		)
::End

:EOF1
	ECHO Could Not Enable Network Adapters....Manually Enable Ethernet Adapters.
	GOTO EOF
:EOF2
	ECHO Network Adapters Enabled
	GOTO EOF
:EOF
@ECHO ON