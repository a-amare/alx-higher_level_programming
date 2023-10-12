#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    if a < b:
        return add(a, b)
    else:
        return sub(a, b)