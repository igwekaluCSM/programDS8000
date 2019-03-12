:: This batch file is intended to intepret the computer specific Ethernet Adpater name.
:: The script will enable all Ethernet connections and disable Wi-Fi connections 

@ECHO OFF 

GOTO firstSearch || GOTO secondSearch  

:firstSearch (
	FOR /F "tokens=4*" %%N IN ('netsh int show int^| findstr "Local Ethernet"') DO (
		SET netName= \"%%N %%O\" && ECHO Network Adapter Name: %netName% && netsh int set int %netName% admin=ENABLED
		IF %ERRORLEVEL% EQU 0 ( ECHO Network Card Enabled) ELSE ( ECHO Couldn't Enable Network Adapter Card )
	)
)
:secondSearch (
	FOR /F "tokens=1,5*" %%P IN ('netsh int ipv4 show int ^| findstr "Local Ethernet"') DO (
		SET idName=%%P &&  ECHO Network Adapter ID Number: %idName% && netsh int set int %idName% admin=ENABLED
		IF %ERRORLEVEL% EQU 0 ( ECHO Network IPv4 Enabled ) ELSE ( ECHO Couldn't Enable Network IPv4 Card) 
		)
)
@ECHO ON