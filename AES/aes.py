#!/usr/bin/env python3

# fontes: 
# https://pypi.python.org/pypi/pycrypto
# https://stuvel.eu/python-rsa-doc/usage.html

import rsa
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

def encrypt( file_, pub_key ):
    aes_key = rsa.randnum.read_random_bits(128) 
    obj = AES.new(aes_key, AES.MODE_CBC, 'This is an IV456')
    msg = b64encode(file_.read().encode('utf-8'))
    msg = msg + bytes(''.join(['$' for i in range(16-len(msg)%16)]).encode('utf-8'))
    f = open("enc01","wb")
    f.write(obj.encrypt(msg))
    return rsa.encrypt(aes_key, pub_key)

    
def decrypt( file_, aes_key ):
    ciphertext = file_.read()
    obj = AES.new(aes_key, AES.MODE_CBC, 'This is an IV456')
    msg = obj.decrypt(ciphertext)
    msg = b64decode(msg)
    print("Texto original: ",end="")
    print(msg)
    


if __name__ == '__main__':

    rsa_k = None

    (pub_key, pvt_key) = rsa.newkeys(2048)

    while True : 
        opcao = input("1 - encrypt file\n2 - decrypt file\n> ")
        fname = input("File name: ")

        if opcao == '1':
            f = open(fname)
            rsa_k = encrypt(f, pub_key)


        elif opcao == '2':
            f = open(fname,"rb")
            decrypt(f, rsa.decrypt(rsa_k, pvt_key))
     
