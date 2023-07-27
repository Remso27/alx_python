#!/usr/bin/python3
def raise_exception():
    a = 12
    name = "Rémi"
    try:
        result = a + name
        raise TypeError ("Here")
    except NameError as NE:
        print("Exeption")
        raise NE