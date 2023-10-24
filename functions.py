x = {}

def _and(*args):
    val = True
    for item in args:
        val = val and item
    return val

def _or(*args):
    val = False
    for item in args:
        val = val or item
    return val

def _print(phrase):
    print(phrase, end="", )

def _input():
    inp = input()
    if inp=="y":
        return True
    elif inp=="n":
        return False
    else:
        print("Вы ввели неверный формат, введите новый ответ: ", end="")
        _input()

def _input_num():
    inp = int(input())
    return inp

def _assign(a, b):
    x[a] = b

def _fact_not_exist(fact):
    return (not fact in x.keys())

def _more(a, b):
    return get(a)>=b

def _less(a, b):
    return get(a)<=b

def _equal(a, b):
    return get(a)==b

def get(param):
    if (param in x.keys()):
        return x[param]
    else:
        return None

all_functions = {
    "and" : _and,
    "or": _or,
    "input": _input,
    "input_num": _input_num,
    "assign": _assign,
    "fact_not_exist": _fact_not_exist,
    "more": _more,
    "less": _less,
    "equal": _equal,
    "print": _print
}