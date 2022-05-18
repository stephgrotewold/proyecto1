from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key=file.read()
file.close()


def encriptar(string):
    fernet = Fernet(key)
    encrypted=fernet.encrypt(bytes(string, 'utf-8'))
    return encrypted

def desencriptar(string):
    fernet = Fernet(key)
    if(string!="b''"):
        decrypted=fernet.decrypt(string)
        return decrypted.decode()


        

