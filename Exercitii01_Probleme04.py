x = int(input("Sa se dea numerele "))
precedent = x
x = int(input())
V = []
while x != -1:
    r = x - precedent
    V.append(r)
    precedent = x
    x = int(input())

ok = 3

for i in range(1, len(V)):
    if V[i] == V[i-1]:
        ok = 1
    else:
        ok = 0
        break

if ok == 1:
    print("Termenii unei progresii aritmetice")
else:
    print("Nu sunt termenii unei progresii aritmetice")