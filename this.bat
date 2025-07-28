
@echo off

:: Delete old task if it exists
schtasks /Delete /TN "PrankParth" /F >nul 2>&1

:: Create new task that runs your Python script in the right folder
schtasks /Create /TN "PrankParth" ^
 /TR "cmd.exe /c \"cd /d C:\Users\manot\Prank-On-Parth && C:\Users\manot\Prank-On-Parth\thisVenv\Scripts\python.exe main.py > prank.log 2>&1\"" ^
 /SC ONCE /ST 00:00 ^
 /RL HIGHEST ^
 /RU "manot" ^
 /RP "ParthIsh@2006" ^
 /F

:: Run the task immediately
schtasks /Run /TN "PrankParth"
