import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("Мөрийн нийлбэр:", np.sum(a, axis=1))
print("Баганын дундаж:", np.mean(a, axis=0))