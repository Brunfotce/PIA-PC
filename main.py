import argparse
import analizador_urls
import encriptar
import envio_prueba
import Escaneo
import subprocess as sp
import os
from powershellHash import valor_hash

#opciones
def main():
    if __name__ == '__main__':
        try:
            import requests
            import openpyxl
            import json
            import cryptography
            import shutil
            import nmap
            import socket
            import scapy
            print("\nCuentas con todos los modulos")
        except ImportError:
            print('\nFaltan modulos')
            os.system("pip install -r requirements.txt")
            print("Los modulos se han instalado correctamente!")
    parser = argparse.ArgumentParser(description = " Opciones: ")
    parser.add_argument("-Opc",type=int, help='-Opc[1=API VIRUS TOTAL, 2= ENCRIPTAR, 3=CORREOS, 4=HASH, 5=ESCANER]')
    data = parser.parse_args()
    parser.add_argument("-hash", type=str, help='-hash "Ingresa la ruta para sacar hash"')
    if(data.Opc == 1):
        analizador_urls.Virus_Total()
    elif(data.Opc == 2):
        encriptar.Cifrado()
    elif(data.Opc == 3):
        envio_prueba.Enviar_Correo()
    elif(data.Opc == 4):
        valor_hash()
    elif(data.Opc == 5):
        Escaneo.ip_scan()
    else:
        pass



main()
