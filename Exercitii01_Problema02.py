import math

r = float(input("Scrieti raza cercului"))
n = int(input("Scrieti numarul de perechi cerc - patrat"))

l = (r*2)/math.sqrt(2)
print("1: raza = ", r, ", latura = ", l)

for i in range(1, n):
    r = l/2
    l = (r*2)/math.sqrt(2)
    print(i+1,": raza = ", r, ", latura = ", l)
