import numpy as np
a = np.array([12, 7, 25, 18, 30, 9, 14, 21])
print(np.sort(a))
print(np.sort(a)[::-1])
print(np.sum(a[a % 2 == 0]))
print(np.sum(a[a % 2 == 1]))