#! /usr/bin/env python3

import math

if __name__ == '__main__':
    txt = input('Digite o texto a ser cifrado:\n')
    key = int(input('Digite a chave:\n'))
   
    for j in range(0, key):
        for i in range(0, math.floor(len(txt)/key)):
            print(txt[i*key+j],end="")
        #print() debug: mostra a matriz transposta ao contrário da sequencia de caracteres





