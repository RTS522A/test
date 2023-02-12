@echo off
@chcp 65001>nul
::echo on

FOR /F "delims=|" %%A IN ("%1") DO (
    SET lastsum=%%~nxA
)
IF NOT "%lastsum%"=="" ( set lastsum=\)

for /f "tokens=1,* delims=\" %%i in ("%~1") do SET SHORTDIR=%%j

IF "%2" == "false" (
for /f "tokens=*" %%i in ('dir %~1 /a:-d /b 2^>nul') do (
echo "%~1%lastsum%%%i" "\%SHORTDIR%%lastsum%%%i"
)
) ELSE (
for /f "tokens=*" %%i in ('dir %~1 /a /b 2^>nul')  do (
echo "%~1%lastsum%%%i" "\%SHORTDIR%%lastsum%%%i"
)
)





