#!/usr/bin/env python3

import sys

if len(sys.argv) == 3 :
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    lst = []

    for i in range(start, end + 1) :
        lst.append(i)

    print(lst)
else :
    print("none")