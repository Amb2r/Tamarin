import numpy as np
import random as rnd
import Func

Env = np.array ([[100 , 99 , 'MR2' , 97, 'NDR3' ,95 , 94 , 93,  92 ,91 ] , [ 81, 82, 83, 84, 85, 86, 87, 88, 89, 90] , [80, 79, 78, 77, 78, 75, 74, 'MR3', 72, 71] , [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [60, 'NDR2', 58, 'NDR3', 'MR1', 55, 54, 53, 52, 51], [41, 42, 43, 44, 'NDR1', 46, 47, 48,49, 50], ['MR2', 39, 38, 37, 36, 35, 34, 33, 32, 31 ], [21, 22, 23, 24, 25, 26, 27, 28 ,29, 30], ['NDR2', 19, 18, 17, 16, 'MR3', 14, 13, 12, 11], ['01', '02', '03', '04', '05', 'NDR1', '07', 'MR1', '09', 10]] , dtype = str)
print (Env)
Tasnum = range(1 , 7)
posP1 = 1 
posP2 = 1
nobat = 1

while True :
    if nobat == 1 :
        
        print (f"Position P1 : {posP1}")
        input ("playe 1 ba ENTER tas briz : ")
        Tas = rnd.choice (Tasnum)
        print (f"Tas : {Tas}" )

        while Tas == 6 :
            Tas = Tas + rnd.choice(Tasnum)

        posP1 = posP1 + Tas

        if posP1 == 100 :
            print ( " palyer 1 is Winner ")
            break
        posP1 = Func.game(posP1)
        print ( f"New positoin of Player 1 : {posP1}")
        nobat = 2

    elif nobat == 2 :
        print (f"Position P1 : {posP2}")
        input ("playe 2 ba ENTER tas briz : ")
        Tas = rnd.choice (Tasnum)
        print (f"Tas : {Tas}" )

        while Tas == 6 :
            Tas = Tas + rnd.choice(Tasnum)

        posP2 = posP2 + Tas

        if posP2 == 100 :
            print ( " palyer 1 is Winner ")
            break
        posP2 = Func.game(posP2)
        print ( f"New positoin of Player 1 : {posP2}")
        nobat = 1


    