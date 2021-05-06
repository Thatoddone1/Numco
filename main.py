import rsa
import pyperclip as pc
encoded = ""
decoded = ""



while True:
    encOrDec = input("Do you want to encode or decode (e/d) ")
    encoded = ''
    decoded = ''
    if encOrDec == "e":
        text = input("what do you want to encode? ")
        text = text.encode("utf8")
        pubkey = input("whats your pubkey? ")   
        encode = rsa.encrypt(text, pubkey)
        print(pubkey, privkey)
        pc.copy(encoded)
        print(encoded)


    elif encOrDec == "d":
        text = input("what do you want to decode? ")
        privkey = input("whats your privkey? ")
        decoded = rsa.decrypt(text, privkey)
        decoded = decoded.decode("utf8")
        print(decoded)
    elif encOrDec == "g":
        (pubkey, privkey) = rsa.newkeys(2048)
        print (pubkey)
        print("")
        print(privkey)
