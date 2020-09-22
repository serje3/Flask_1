from Encryption.writeCode import writec
from Encryption.loadCode import loadc
from Encryption.crypt import encrypt,decrypt
import random as rm
def enc(word):
    ind = rm.randint(2 ** 23, 2 ** 57)
    writec('ks/'+str(ind))
    return [encrypt(word, loadc('ks/'+str(ind))), ind]
def dec(word,key):
    return decrypt(word,loadc('ks/'+str(key)))