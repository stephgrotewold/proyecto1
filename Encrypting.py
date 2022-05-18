from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "contraseña"  # En base a la password se genera la key
password = password_provided.encode()
salt = b'\xd6l:S\x10\x1e!\xf8\x05X\xf8\xb4\xce\xb43T'  #Generado utilizando os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password)) 

def encriptar(string):
    fernet = Fernet(key)
    encrypted=fernet.encrypt(bytes(string, 'utf-8'))
    return encrypted

def desencriptar(string):
    fernet = Fernet(key)
    if(string!="b''"):
        decrypted=fernet.decrypt(string)
        return decrypted.decode()
