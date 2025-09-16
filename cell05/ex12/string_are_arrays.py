#!/usr/bin/env python3

import sys

if len(sys.argv) == 2 :
    str = sys.argv[1]
    result = ""
    for ch in str :
        if ch == 'z' :
            result += ch

    if len(result) == 0 :
        print("none")
    else :
        print(result)
else :
    print("none")