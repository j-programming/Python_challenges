#!/usr/bin/env python
#ROT13
import sys

def decrypt(encrypted_text):
    plain_text=''
    for char in encrypted_text:
        plain_text+=chr(ord(char)-13)
    print(plain_text)
    return

def encrypt(plain_text):
    encrypted_text=''
    for char in plain_text:
        encrypted_text+=chr(ord(char)+13)
    print(encrypted_text)
    return    



def main(args):
    if len(args)==3:
        if (args[1]=='-e'):
            encrypt(args[2])
        elif (args[1]=='-d'):
            decrypt(args[2])
        else:
            print('Usage: 61.py [options] text \n-e - Encypt text\n-d - Decrypt text')
    else:
        print('Usage: 61.py [options] text \n-e - Encypt text\n-d - Decrypt text')

if __name__ == "__main__":
    main(sys.argv)
