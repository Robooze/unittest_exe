def gen_to_list(num):
    return list(range(num))


def division(a, b):
    return a / b


def int_division(a, b):
    return a // b


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


def dict_division(**dizionario):
    a = dizionario["a"]
    b = dizionario["b"]
    return {"a": a, "b": b, "r": division(a, b)}
