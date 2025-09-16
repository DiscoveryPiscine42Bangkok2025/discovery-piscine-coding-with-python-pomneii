#!/usr/bin/env python3

import sys

if len(sys.argv) > 2 :
    lst = sys.argv[:0:-1]
    for str in lst :
        print(str)

else :
    print("none")