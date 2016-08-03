#! /usr/bin/env python3

M = 1099511627776
B = 3

def diffie_hellman (base, exp):
    return (base ** exp)%M; 

def ext_key ( k ):
    return diffie_hellman(B, k)

def check_key( alice, bob ):
    print ('Alice key:', diffie_hellman(ext_key(bob), alice))
    print ('Bob key:', diffie_hellman(ext_key(alice), bob))
 
if __name__ == '__main__':
    alice = int(input('type alice key:\n'))
    bob = int(input('type bob key:\n'))
    check_key(alice, bob)
