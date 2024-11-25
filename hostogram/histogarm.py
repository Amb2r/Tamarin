import numpy as np
import matplotlib.pyplot as plt
import Func
file= open('d.txt' , 'r')

for line in file :
    data = line.split(' ')
data = [int (i) for i  in data]
print (data)

plt.style.use('_mpl-gallery')

# make data:
x = 1 + np.arange(9)
y = Func.his(data)


# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=5, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0 , 10), xticks=np.arange(0, 10),
       ylim=(0, 40), yticks=np.arange(1,40))

plt.show()
# x =  1 + np.arange(9)
# y = Func.his(data)
# plt.style.use('_mpl-gallery')

# # make data
# x = 1 + np.arange(9)
# y = Func.his(data)
# print (y)
# print (x)

# # plot
# fig, ax = plt.subplots()

# ax.stem(x, y)

# ax.set(xlim=(0, 30), xticks=np.arange(1, 30),
#        ylim=(0, 40), yticks=np.arange(1, 40))

# plt.show()