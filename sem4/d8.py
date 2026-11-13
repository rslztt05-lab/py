n = int(input("Too: "))
k = 0
while n > 0:
    k += 1
    n //= 10
print(k)