#!/usr/bin/env python3

def find_the_redheads(dict) :
    lst = []
    for name, color in dict.items() :
        if color == "red" :
            lst.append(name)

    return lst

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))