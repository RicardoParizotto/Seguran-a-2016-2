#!/usr/bin/env python3

# fontes: 
# https://pypi.python.org/pypi/pycrypto
# https://stuvel.eu/python-rsa-doc/usage.html

import rsa
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import sys
import hashlib




if __name__ == '__main__':

    f = open(sys.argv[1], "r")

    signature = f.readline()
    
    e = f.readline()

    m = f.readline()

    message = f.read()
    
    pubkey = rsa.PublicKey(int(e), int(m))

    print(pubkey)

    print(signature)

    print(rsa.decrypt(bytes(signature.encode("UTF-8")), pubkey))


    #if(rsa.decrypt(signature, pubkey) == hashlib.sha256(message.encode("UTF-8")).hexdigest()) :
        #print ("cuzinho")


