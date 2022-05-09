import subprocess

def valor_hash512():
    comando = "Hash512.ps1"
    lineaPS = "powershell -Executionpolicy ByPass -file "+ comando
    runningProcesses = subprocess.check_output(lineaPS)
    print(runningProcesses.decode())

