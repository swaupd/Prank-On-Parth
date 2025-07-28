@echo off

REM Delete old task if it exists
schtasks /Delete /TN "PrankParth" /F

REM Create the scheduled task
schtasks /Create /TN "PrankParth" /TR "cmd /c cd /d C:\Users\manot\Prank-On-Parth && C:\Users\manot\Prank-On-Parth\thisVenv\Scripts\python.exe main.py" /SC ONCE /ST 00:00 /RL HIGHEST /F /RU manot /RP ParthIsh@2006

REM Run the task
schtasks /Run /TN "PrankParth"
