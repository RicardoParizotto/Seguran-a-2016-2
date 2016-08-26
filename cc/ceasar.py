#! /usr/bin/env python3

key = 5

aux = []

if __name__ == '__main__':
    txt = input('Digite o texto a ser cifrado:\n')
    for i in range(0, len(txt)):
        aux.append(chr((ord(txt[i]) + key) % 256))

    print(aux)

