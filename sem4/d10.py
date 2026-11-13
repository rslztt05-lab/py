n = int(input("Too: "))
x, r = n, 0
while x > 0:
    r = r * 10 + x % 10
    x //= 10
print("Ijil" if r == n else "Ijil bish")