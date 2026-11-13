import numpy as np
a = np.array(["Apple", "Banana", "Cat", "Watermelon"])
print([len(x) for x in a])
print(min(a, key=len))
print(max(a, key=len))
print(" ".join(a))