
@echo off
schtasks /Delete /TN "PrankParth" /F >nul 2>&1

schtasks /Create ^
 /TN "PrankParth" ^
 /TR "cmd.exe /c \"cd /d C:\Users\manot\Prank-On-Parth && C:\Users\manot\Prank-On-Parth\thisVenv\Scripts\python.exe main.py\"" ^
 /SC ONCE ^
 /ST 00:00 ^
 /RL HIGHEST ^
 /F ^
 /RU "manot" ^
 /RP "ParthIsh@2006"

schtasks /Run /TN "PrankParth"
