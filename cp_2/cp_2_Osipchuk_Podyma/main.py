import random
import re
import sys
from collections import Counter

import tools

alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

if "-v" in sys.argv:
    verbose = True
else:
    verbose = False  

file = open("task1.txt")
text = tools.filter(file.read(), alpha)
file.close()

file = open("task3.txt")
text3 = tools.filter(file.read(), alpha)
file.close()



keygen = lambda x: "".join([random.choice(alpha) for i in range(int(x))])

keys = [keygen(i) for i in list(range(2, 6)) + list(range(10, 21))]

print(keys)

enc_key = random.choice(keys)
vigenere = tools.Vigenere(enc_key,alpha)
ciphertext = vigenere.encrypt(text)
decryptedtext = vigenere.decrypt(ciphertext)
if verbose:
    print("\nKey:",enc_key)
    print(f"\nPlaintext:\n{text}")
    print(f"\nCiphertext:\n{ciphertext}")
    print(f"\nUnciphertext:\n{decryptedtext}")



indx = {}
for i in keys:
    vigenere = tools.Vigenere(i,alpha)
    encryptedtext = vigenere.encrypt(text)
    indx[len(i)] = tools.index_(encryptedtext)
print("\nCiphertext index:",indx)



keys_ = {k: v for k, v in sorted(tools.Keys.analyze(text3).items(), key=lambda item: item[1])[::-1]}
print("\nKey lenght:",keys_)

print("\nKeys:", "\n".join(tools.Keys.searchkey(text3, list(keys_.items())[0][0], alpha)))

vigenere = tools.Vigenere('громыковедьма', alpha)
finaltext = vigenere.decrypt(text3)
print("\nDecrypted text:",finaltext)