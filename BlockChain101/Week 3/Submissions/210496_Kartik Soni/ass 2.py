
from Crypto.PublicKey import RSA
from cryptography.fernet import Fernet
private_key=input("")
secret_code=input("")
encoded_key = open(private_key,"rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)
v=key.publickey().export_key()
print(key.publickey().export_key())
fernet=Fernet(v)
print(fernet.encrypt(message.encode()))
