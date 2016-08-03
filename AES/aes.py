#!/usr/bin/env python3

from Crypto.Cipher import AES
from base64 import b64encode, b64decode

opcao = input("1 - Encriptar um arquivo\n2 - Decriptar um arquivo\n> ")
fname = input("Digite o nome do arquivo: ")

chave = input("Digite uma chave para encriptar/decriptar o texto: ")
chave = chave + ''.join(['0' for i in range(16-len(chave)%16)])

if opcao == '1':
    # Adaptado de https://pypi.python.org/pypi/pycrypto
    obj = AES.new(chave, AES.MODE_CBC, 'This is an IV456')
    f = open(fname)
    message = b64encode(f.read().encode('utf-8'))
    message = message + bytes(''.join(['$' for i in range(16-len(message)%16)]).encode('utf-8'))
    ciphertext = obj.encrypt(message)
    print("Texto encriptado: %s"%ciphertext)
    f = open("enc01","wb")
    f.write(ciphertext)
elif opcao == '2':
    f = open(fname,"rb")
    ciphertext = f.read()
    obj2 = AES.new(chave, AES.MODE_CBC, 'This is an IV456')
    texto = obj2.decrypt(ciphertext)
    strt = str(texto).split('$')[0].split("'")[1]
    texto = b64decode(strt)
    print("Texto original: ",end="")
    print(texto)
