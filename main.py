from Crypto.PublicKey import RSA
import pyperclip as pc
from Crypto.Cipher import PKCS1_OAEP
encoded = ""
decoded = ""



while True:
    encOrDec = input("Do you want to encode or decode (e/d) ")
    if encOrDec == "e":
        text = input("what do you want to encode? ")
        encryptor = PKCS1_OAEP.new(pubkey)
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
        print(pubKeyPEM)
        f = open('mykey.pem','wb')
        f.write(key.export_key('PEM'))
        f.close()
    elif encOrDec == "i":
        f = open('mykey.pem','r')
        privkey = f.read()
        f.close()
    elif encOrDec == "c":
        outerpubkey = input("What is the recivers public key")
        pubkey = outerpubkey
