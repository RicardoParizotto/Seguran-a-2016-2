#! /usr/bin/env python3

key = "56"

aux = []

if __name__ == '__main__':
    txt = input('Digite o texto a ser cifrado:\n')
    for i in range(0, len(txt)):
        for j in key:
            aux.append(chr((ord(txt[i]) + ord(j)) % 256))

    print(aux)

