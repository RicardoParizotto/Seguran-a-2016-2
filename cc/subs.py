#! /usr/bin/env python3

import random

keys = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]


aux = []



dic = {}

if __name__ == '__main__':
    txt = input('Digite o texto a ser cifrado:\n')
    for i in range(0, len(txt)):
        if chr(txt[i]) not in dic:
            k = random.randint(0, len(keys))
            dic{chr(txt[i])} = keys.pop(i)              

    print(aux)

