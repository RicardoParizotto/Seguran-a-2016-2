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

    x = hashlib.sha256(content.encode("UTF-8")).hexdigest()
   
    signature = rsa.encrypt(x.encode("UTF-8") , pvt_key)   #gera assinatura

    h = open("file", "w+") 
    
    h.write(str(signature)+"\n")

    h.write(str(pub_key.n)+"\n") #modulo da chave pública

    h.write(str(pub_key.e)+"\n") #exponte da chave pública

    h.write(content)  #texto original

    h.close()

