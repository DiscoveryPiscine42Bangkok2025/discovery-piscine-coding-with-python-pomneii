#!/usr/bin/env python3

import sys

def downcase_all(str) :
    return str.lower()

if len(sys.argv) > 2 :
    for str in sys.argv[1:] :
        print(downcase_all(str))
else :
    print("none")