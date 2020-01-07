V = []
x = (input("Sa se scrie codul "))
i = 0
while i < len(x):
    V.append(int(x[i]))
    i += 1


def dimensiune(x):
    if len(x) <= 9:
        return 1
    return 0


def cifra_para(v):
    for i in range(1,len(v)):
        if v[i] % 2 == 0:
            return 1
    return 0


def cifra_impara(v):
    for i in range(1,len(v)):
        if v[i] % 2 == 1:
            return 1
    return 0


def conditie(v):
    produs_pare = 1
    suma_impare = 0
    for i in range(1,len(v)):
        if v[i] % 2 == 0:
            produs_pare *= i
        else:
            suma_impare += i
    if v[0] == 1:
        return 1
    elif produs_pare % v[1] == suma_impare % v[1]:
        return 1
    return 0


if dimensiune(x) == cifra_impara(V) == cifra_para(V) == conditie(V) == 1:
    print("\nCorect")
else:
    print("\nIncorect")
