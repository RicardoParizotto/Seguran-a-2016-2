#!/usr/bin/env python3

from Crypto.Cipher import AES
from base64 import b64encode, b64decode

opcao = input("1 - Encriptar um arquivo\n2 - Decriptar um arquivo\n> ")
f = open(input("Digite o nome do arquivo: "))

chave = input("Digite uma chave para encriptar o texto: ")
chave = chave + ''.join(['0' for i in range(len(chave)%16)])

# Adaptado de https://pypi.python.org/pypi/pycrypto

obj = AES.new(b64encode(chave.encode('utf-8')), AES.MODE_CBC, 'This is an IV456')
message = f.read()
message = message + ''.join(['0' for i in range(len(message)%16)])
ciphertext = obj.encrypt(message)

print("Texto encriptado: %s"%ciphertext)

obj2 = AES.new(chave, AES.MODE_CBC, 'This is an IV456')
obj2.decrypt(b64decode(ciphertext))

