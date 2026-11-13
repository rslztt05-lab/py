# a aas b hurtelh 5 d huvaagdah toonuudin niilber
a = int(input("a: "))
b = int(input("b: "))
niilber = 0
for i in range(a, b + 1):
    if i % 5 == 0:
        niilber = niilber + i
print("Niilber:", niilber)