import numpy as np
A = np.array([[12, 15, 18],[20, 25, 30],[10, 14, 16]])
print("Мөр бүрийн нийлбэр:", A.sum(axis=1))     
print("Багана бүрийн дундаж:", A.mean(axis=0)) 
print(A.max())  
print(A.sum())