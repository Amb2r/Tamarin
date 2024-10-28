def AA(L):
    Z=[0]
    I = 0
    for i in L :
        c = 2 
        y = 1
        while c < L[I] :
            if c %  L[I] == 0 :
                y = 0
            c = c +1
        if y == 0:
           Z.append(L[I])
        I = I + 1
    
    return(Z)



Lis = [0]
i = 0
while i <10000 :
    x = input("please inter your number : ")
    if x == "end" : 
        break
    Lis.append(int(x))
    i = i + 1

Lis.pop(0)
print (Lis)
print (AA(Lis))