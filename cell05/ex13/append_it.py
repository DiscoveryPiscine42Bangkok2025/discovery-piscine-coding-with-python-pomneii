#!/usr/bin/env python3

import sys

if len(sys.argv) > 1 :
    kw = "ism"
    for param in sys.argv[1:] :
        if not param.endswith(kw):
            print(f"{param}ism")
else :
    print("none")