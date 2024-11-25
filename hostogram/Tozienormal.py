import numpy as np
import matplotlib.pyplot as plt
import Func
file= open('d.txt' , 'r')

for line in file :
    data = line.split(' ')
data = [int (i) for i  in data]
print (data)
avg= np.average(data)
var = np.var(data)
print (f"Avg = {avg}")
print (f"Var = {var}")

Data = Func.toz(avg , var , data)
x = np.linspace(-30, 50, 120)
plt.figure()
plt.plot(x , Data)
plt.show()








    