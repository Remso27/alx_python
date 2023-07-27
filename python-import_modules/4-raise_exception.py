#!/usr/bin/python3
def raise_exception():
    a = 12
    name = "Rémi"
    try:
        result = a + name
        raise TypeError ("Here")
    except TypeError as te:
        print("Exeption")
        raise te