Set objShell = CreateObject("WScript.Shell")
strScriptPath = objShell.CurrentDirectory
strBatchScript = strScriptPath & "\execute.bat"

objShell.CurrentDirectory = strScriptPath
objShell.Run """" & strBatchScript & """", 0
