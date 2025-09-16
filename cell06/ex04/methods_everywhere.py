#!/usr/bin/env python3

import sys

def shrink(str) :
    return str[:8]

def enlarge(str) :
    len_z = 8 - len(str)
    return str + ('Z' * len_z)

if len(sys.argv) > 2 :
    for param in sys.argv :
        if len(param) < 8 :
            print(enlarge(param))
        elif len(param) == 8 :
            print(param)
        else :
            print(shrink(param))
else :
    print("none")