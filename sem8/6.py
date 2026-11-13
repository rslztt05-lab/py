import numpy as np
a = np.arange(1, 21)
print("Сондгой:", a[a % 2 == 1])
print(np.sum(a))
print(np.mean(a))