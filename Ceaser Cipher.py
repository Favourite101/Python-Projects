# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 14:32:05 2023

@author: Favourrr
"""

import sys

def encrypt(text, key):
    encrypted = ""
    for i in range(len(text)):
        chare = text[i]
        encrypted += chr((ord(chare) + key - 65) % 26 + 65)
    print(encrypted)
def decrypt(text, key):
    decrypted = ""
    for i in range(len(text)):
        chare = text[i]
        decrypted += chr((ord(chare) - key - 65) % 26 + 65)
    print(decrypted)
option = int(input("Enter 1 to encrypt and 2 to decrypt\n"))
if option < 1 or option > 2:
    print("Invalid!")
    sys.exit()
text = input("Enter text: ")
text = text.upper()
print(text)
key = int(input("Enter the shift number: "))

if option == 1:
    encrypt(text, key)
elif option == 2:
    decrypt(text, key)
