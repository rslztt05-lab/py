n = int(input("N: "))
m = int(input("M: "))
k = 0
for a in range(n, m + 1):
    anhni = a > 1
    for i in range(2, a):
        if a % i == 0:
            anhni = False
            break
    if anhni:
        k += 1
print(k)