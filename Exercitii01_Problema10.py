import math
n = int(input("Dati numarul n "))
k = 0

def prim(numar):
    if numar < 2:
        return 0
    if numar == 2:
        return 1
    for i in range(2, math.floor(numar/2)+1):
        if numar % i == 0:
            return 0
    return 1

print("Dati cele n numere ")

while n:
    x = int(input())
    if prim(x) == 1:
        k += 1
    n -= 1

if k >0:
    print(k, " dintre numerele date sunt prime")
else:
    print("Nu s-au gasit numere prime")


