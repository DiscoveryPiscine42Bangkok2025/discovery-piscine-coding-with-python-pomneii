#!/usr/bin/env python3

import sys

if len(sys.argv) == 1 :
    print("none")
else :
    lst = sys.argv[1:]
    print(f"parameters: {len(lst)}")
    for str in lst :
        print(f"{str}: {len(str)}")