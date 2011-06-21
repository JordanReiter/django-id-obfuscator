from django.conf import settings
import random, re
from id_obfuscator import base58

def generate_secret_key(length=40):
    random.sample(base58.characters, length)
    
def obfuscate(i, length=8, key=settings.ID_OBFUSCATOR_KEY):
    i = int(i)
    if i < 0:
        raise ValueError("Input must be a positive integer.")
    result = ""
    pos = i % len(key)
    combine_key = key[pos:] + key[:pos]
    asc = base58.b58encode(i)
    pos_asc = base58.b58encode(pos)
    if len(asc) < length:
        asc = ("0" * (length-len(asc))) + asc
    for cpos in range(0, len(asc)):
        a_lookup = base58.characters.find(asc[cpos])
        k_lookup = base58.characters.find(combine_key[cpos])
        k = a_lookup + k_lookup
        if k == -1:
            result += '0'
            continue
        k = (k + base58.base) % base58.base
        #print asc[cpos], "(%d) + " % a_lookup , combine_key[cpos], "(%d) =" % k_lookup, base58.characters[k],  "(%d)" % k
        if k - k_lookup == -1 and asc[cpos] != "0":
            result += "."
        result += base58.characters[k]
    result = pos_asc + result
    return result

VALID_HASH_FORMAT=r"^[0%(chars)s](\.?[0%(chars)s])+$" % {'chars': base58.characters}
def deobfuscate(s, key=settings.ID_OBFUSCATOR_KEY):
    if not re.search(VALID_HASH_FORMAT, s):
        raise ValueError("Invalid hash value: %s" % s)
    pos = base58.b58decode(s[0])
    combine_key = key[pos:] + key[:pos]
    #print "The combine key is %s" % combine_key
    s = s[1:]
    asc = ""
    for cpos in range(0, len(s.replace(".",""))):
        if s[cpos] == ".":
            treat_as_number = True
            s = s[:cpos] + s[cpos+1:]
        else:
            treat_as_number = False
        k = base58.characters.find(s[cpos])
        k = k - base58.characters.find(combine_key[cpos]) 
        if not treat_as_number and (k == -1 or s[cpos] == "0"):
            #print s[cpos], "(%d) - " % base58.characters.find(s[cpos]) , combine_key[cpos], "(%d) =" % base58.characters.find(combine_key[cpos]), base58.characters[k],  "(%d)" % k
            continue
        k = (k + base58.base) % base58.base
        #print s[cpos], "(%d) - " % base58.characters.find(s[cpos]) , combine_key[cpos], "(%d) =" % base58.characters.find(combine_key[cpos]), base58.characters[k],  "(%d)" % k
        asc += base58.characters[k]
    result = base58.b58decode(asc)
    return result