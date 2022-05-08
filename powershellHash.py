import subprocess

def valor_hash():
    comando = "Hash.ps1"
    lineaPS = "powershell -Executionpolicy ByPass -file "+ comando
    runningProcesses = subprocess.check_output(lineaPS)
    print(runningProcesses.decode())

