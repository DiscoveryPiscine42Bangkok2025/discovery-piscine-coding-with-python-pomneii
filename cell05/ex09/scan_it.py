#!/usr/bin/env python3

import sys
import re

if len(sys.argv) > 2 :
    kw = sys.argv[1]
    str = sys.argv[2]

    if len(re.findall(kw, str)) == 0 :
        print("none")
    else :
        print(len(re.findall(kw, str)))
else :
    print("none")