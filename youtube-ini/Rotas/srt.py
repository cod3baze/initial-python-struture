#duas fomas de criar nomes aleatórios com o abc..
# 1 -> só escolhe duas letras.
# 2 -> ecolhe quantas letras quiser.

def srtT_name_():
    from random import randrange as rng

    lst = "abcdefghijklmnoprstuvxwyz"
    srt = list()

    while True:
        n = rng(0, len(lst))
        srt.append(lst[n])
        if len(srt) == 2:
            name = "".join(srt)
            break

    return name


def srt_name(n):
    from random import randrange as rng

    lst = "abcdefghijklmnoprstuvxwyz"
    srt = list()

    while True:
        n = rng(0, len(lst))
        srt.append(lst[n])
        if len(srt) == n:
            name = "".join(srt)
            break

    return name

x = srt_name(3)
nm = srtT_name_()
print(nm)
print(x)