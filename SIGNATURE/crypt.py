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

    rsa_k = None

    (pub_key, pvt_key) = rsa.newkeys(1024)
    
    f = open(sys.argv[1], "r")
    
    content = f.read()

    f.close()

    signature = rsa.sign(content.encode("UTF-8"), pvt_key, 'SHA-1')   #gera assinatura
    
    g = open("signature", "wb") 

    g.write(str(signature).encode("UTF-8"))    #salva assinatura

    h = open("file", "wb") 
    
    h.write(str(pub_key.n).encode("UTF-8")) #modulo da chave pública

    h.write(str(pub_key.e).encode("UTF-8")) #exponte da chave pública

    h.write(content.encode("UTF-8"))  #texto original

