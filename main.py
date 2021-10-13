from Crypto.PublicKey import RSA
import pyperclip as pc
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode
encoded = ""
decoded = ""



while True:
    encOrDec = input("Do you want to encode or decode (e/d) ")
    if encOrDec == "e":
        text = input("what do you want to encode? ")
        encryptor = PKCS1_OAEP.new(pubkey.publickey())
        encrypted = encryptor.encrypt(text)
        pc.copy(encrypted)
        print(encrypted)
    elif encOrDec == "d":
        text = input("what do you want to decode? ")
        decryptor = PKCS1_OAEP.new(privkey)
        decoded= decryptor.decrypt(text)
        print(decoded)
    elif encOrDec == "g":
        key = RSA.generate(2048)
        pubkey = key.publickey()
        pubKeyPEM = pubkey.exportKey()
        finalprivkey = b64encode(pubKeyPEM)
        print(finalprivkey)
        f = open('mykey.pem','wb')
        f.write(key.export_key('PEM'))
        f.close()
    elif encOrDec == "i":
        f = open('mykey.pem','rb')
        readprivkey = f.read()
        privkey = RSA.import_key(readprivkey)
        f.close()
    elif encOrDec == "c":
        outerpubkey = input("What is the recivers public key")
        tobepubkey = b64decode(outerpubkey)
        pubkey = RSA.import_key(tobepubkey)
        
