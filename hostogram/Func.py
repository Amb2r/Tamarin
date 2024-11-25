import numpy as np
def toz(a , v , data):
    D = []
    for i in data :
        x = (1/(v*np.sqrt(2*np.pi)))*((2.718)**(((i - a)/v)**2)/2)
        D.append(x)
    return (D)

def his (data) :
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    x7 = 0
    x8 = 0
    x9 = 0

    for i in data : 
        if i < -10 :
            x1 = x1 +1
        if  -10 <= i < -5 :
            x2 = x2 +1
        if  -5 <= i < 0 :
            x3 = x3 +1
        if 0 <= i < 5 :
            x4 = x4 +1
        if 5 <= i < 10 :
            x5 = x5 +1
        if 10 <= i < 15 :
            x6 = x6 +1
        if 15 <= i < 20 :
            x7 = x7 +1
        if 20 <= i < 25 :
            x8 = x8 +1
        if 25 <= i :
            x9 = x9 +1
    return ([x1, x2, x3, x4, x5, x6, x7, x8, x9])