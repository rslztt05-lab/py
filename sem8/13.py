import numpy as np
a = np.array([250, 320, 180, 400, 350, 500, 280])
print("Нийт:", a.sum())                      
print("Дундаж:", a.mean())                
day = a.argmax()
print("Хамгийн их өдөр:", day + 1, a.max())  
print("300-аас дээш өдрийн тоо:", (a > 300).sum())  
n_a = a * 1.10
print("Шинэ массив:", n_a)