#!/usr/bin/env python3

def array_of_name(dict) :
    name_lst = []
    for first, last in dict.items() :
        name_lst.append(f"{first.capitalize()} {last.capitalize()}")
    return name_lst

person = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_name(person))