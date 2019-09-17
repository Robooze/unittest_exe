"""
This is gonna be a library of functions to test in the Unit Test
"""


def gen_to_list(num):
    return list(range(num))


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Cannot divide by 0!")


def int_division(a, b):
    try:
        return a // b
    except ZeroDivisionError as e:
        print("Cannot divide by 0!")


def dict_division(**dizionario):
    '''
    {
    a=4
    b=2
    }

    result:
    {
    a=4
    b=2
    r=2
    }
    '''
    a = dizionario["a"]
    b = dizionario["b"]
    return {"a": a, "b": b, "r": division(a, b)}
