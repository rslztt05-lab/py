import numpy as np
a = np.random.randint(1, 11, 10)
print(a[a > 5])
a[a < 5] = 0
print(a)