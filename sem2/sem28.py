# ugugdsun too anhnii tun mun bish eseh
n = int(input("n: "))
toolol = 0
for i in range(1, n + 1):
    if n % i == 0:
        toolol = toolol + 1

if toolol == 2:
    print(n, "ni anhnii too")
else:
    print(n, "ni anhnii too bish")