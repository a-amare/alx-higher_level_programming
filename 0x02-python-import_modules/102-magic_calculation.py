#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))


def add(a, b):
    return a + b

def sub(a, b):
    return a - b