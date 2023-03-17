@echo off
setlocal EnableDelayedExpansion

rem Set the log file path
set "logFile=logging.csv"

rem Initialize the loop counter
set "loopCounter=1"

rem Delete old logging.csv if it exists
if exist "%logFile%" (
del "%logFile%"
)

:loop
for /f "tokens=1-3 delims=/ " %%a in ('date /t') do (
  set "day=%%a"
  set "month=%%b"
  set "year=%%c"
)
rem Get the current time
for /f "tokens=1-2 delims=: " %%a in ('time /t') do (
  set "hour=%%a"
  set "minute=%%b"
)

rem Check if the current time is past the stop time 17:00
if %hour% GEQ 17 (
  echo Stopping logging process.
  goto :done
)

rem Run the tasklist command and output to a temporary file
tasklist /v /fo csv > temp.csv

rem Parse the output and write to the log file
(for /f "skip=1 tokens=1-10 delims=," %%a in (temp.csv) do (
  rem Write the loop counter, current time, and process information to the log file
  echo %%a,!loopCounter!,!day!.!month!.!year!,!hour!:!minute!,%%e,%%g
)) >> %logFile%

rem Delete the temporary file
del temp.csv

rem Increment the loop counter
set /a "loopCounter+=1"

rem Wait for 1 minute before running the loop again
ping -n 61 127.0.0.1 > nul

goto :loop

:done

rem run python file
py data_transformation.py

rem Done
echo Logging process stopped.
