import numpy as np
a = np.array([65, 78, 90, 55, 88, 72, 95, 60, 83, 47])
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(a[a > 70])
print(np.sum(a < 60))
print("Өсөх дараалал:", np.sort(a))