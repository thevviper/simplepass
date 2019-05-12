#!/usr/bin/env python
# coding: utf-8
import hashlib
import random
import sys
import time

PUNCTUATIONS = "`~!@#$%^&*()-=_+[]{};:./<>?|"


args = list(sys.argv)

capital = "--lowercase" not in args
punc = "--no-puncs" not in args
max_len = 32
for arg in args[1:]:
    try:
        int_arg = int(arg)
    except:
        continue
    max_len = int_arg
    break

e = str(time.time() + random.randint(0, 2**32))

pw = list(hashlib.sha512(e).hexdigest())
if len(pw) > max_len:
    ids = [i for i in range(len(pw))]
    random.shuffle(ids)
    ids = ids[:max_len]
    res = []
    for i in ids:
        res.append(pw[i])
    pw = res
    
if punc:
    p = 1 + random.randint(0, 3)
    ids = [i for i in range(len(pw))]
    random.shuffle(ids)
    ids = ids[:p]
    for i in ids:
        pw[i] = PUNCTUATIONS[random.randint(0, len(PUNCTUATIONS) - 1)]
        
if capital:
    alphas = []
    for i in range(len(pw)):
        if pw[i].isalpha():
            alphas.append(i)
    random.shuffle(alphas)
    caps = len(alphas) // 2
    alphas = alphas[:caps]
    for i in alphas:
        pw[i] = pw[i].upper()

print("".join(pw))
