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
    
    g = open(sys.argv[2], "r")

    signature = f.read()
    
    e = g.read(308) #expoente

    m = g.read(5) #modulo
    
    pubkey = rsa.PublicKey(int(e), int(m))

    print(signature)

    message = g.read()

    print(rsa.verify(message, signature, pubkey))

