import sys

def padrao(palavra):
    d = {}
    s = ""
    c = 0
    for l in palavra:
        if l not in d:
            d[l] = c
            c += 1
        s += str(d[l])
    return s

for k in sys.argv[1:]:
    print(k+" -> "+padrao(k))
