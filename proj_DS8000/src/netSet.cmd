:: This batch file is intended to intepret the computer specific Ethernet Adpater name.
:: The script will enable all Ethernet connections and disable Wi-Fi connections 
:: test of batch comments

@ECHO OFF
FOR /F "tokens=4*" %%N IN ('netsh int show int^| findstr "Local Ethernet"') DO (  
	ECHO here: %~2
	IF %ERRORLEVEL% EQU 0 (
		SET netName= \"%%N %%O\"
		ECHO netName1: %netName%
		TIMEOUT 1
		netsh int set int %netName% admin=ENABLED >> "ipNetSet.txt"
		) ELSE (
			FOR /F "tokens=1,5*" %%P IN ('netsh int ipv4 show int ^| findstr "Local Ethernet"') DO (
				SET idName=%%P
				ECHO idName: %idName%
				netsh int set int %idName% admin=ENABLED
				TIMEOUT 1
				)
		)
	)
::SET netName=
::SET idName=
)
@ECHO ON