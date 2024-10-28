import numpy as np

def Avg(L):
    return (np.average(L) )
def Max(L) :
    return (np.max(L))
def Min(L) :
    return (np.min(L))
def Var(L) :
    return (np.var(L))


Lis = [0]
i = 0
while i <10000 :
    x = input("please inter your number : ")
    if x == "end" : 
        break
    Lis.append(int(x))
    i = i + 1

Lis.pop(0)
print ( Lis)

print (f"Average is : {Avg (Lis)}")
print (f"Maximum is : {Max (Lis)}")
print (f"Minimum is : {Min (Lis)}")
print (f"Varianse is : {Var (Lis)}")
