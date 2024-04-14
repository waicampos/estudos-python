#testando a proteção de branchs no github

def soma(**kwargs):
    print(kwargs)


def sub(*args):
    total = args[0]
    for v in args[1:]:
        total -= v

    return total

def sum(*args):
    print(args, type(args))
    total = 0
    for v in args:
        total += v

    return total


print(soma(x=2, i=4))
print(sum(1, 20, 1, 5, 3))
print(sub(1, 20, 1, 5, 3))
