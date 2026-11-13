n = int(input("Too: "))
anhni = n > 1
for i in range(2, n):
    if n % i == 0:
        anhni = False
        break
print("Anhnii too" if anhni else "Anhnii too bish")