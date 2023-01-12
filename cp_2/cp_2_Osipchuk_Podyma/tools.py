import re
from collections import Counter


class Vigenere:
    def __init__(self, key, alpha="абвгдежзийклмнопрстуфхцчшщъыьэюя"):
        self.key = key
        self.alpha = alpha
        self.N = len(self.alpha)

    
    def encrypt(self, text):
        et = [self.alpha[(self.alpha.index(text[i]) + self.alpha.index(self.key[i % len(self.key)])) % self.N] for i in range(len(text))]
        return ''.join(et)
   

    def decrypt(self, text):
        decryptedtext = [self.alpha[(self.alpha.index(text[i]) - self.alpha.index(self.key[i % len(self.key)]) % self.N)] for i in range(len(text))]
        return ''.join(decryptedtext)


class Keys:
    def split_(text, l):
        return [text[i::l] for i in range(l)]
    

    def searchkey(text, ln, alpha):
        s = Keys.split_(text, ln) 
        possiblekeys = []
        for l in 'оеа':
            key = ""
            for k in s:
                countblock = Counter(k)
                key += alpha[(alpha.index(max(countblock, key= countblock.get)) - alpha.index(l)) % len(alpha)]
            possiblekeys.append(key)            
        return possiblekeys

    
    def analyze(text):
        r = {}
        for i in range(1, 21):
            s = Keys.split_(text, i)
            n = 0
            for k in s:
                n += index_(k)
            n /= i
            r[i] = n
        return r   



def index_(text):
    d = Counter(text)
    ind = 0
    for i in d:
        ind += d[i] * (d[i] - 1)
    ind /= (len(text) * (len(text) - 1))
    return ind



def filter(text, alpha):
    return re.sub(f"[^{alpha}]", "", text)