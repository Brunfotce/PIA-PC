from cryptography.fernet import Fernet
import shutil


def Cifrado():
    shutil.copyfile('reporte_analizador_urls.csv', 'reporte_analizador_urls_encriptado.csv')

    key=Fernet.generate_key()

    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open('reporte_analizador_urls_encriptado.csv', 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open('reporte_analizador_urls_encriptado.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
