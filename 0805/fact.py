def fact(x):
    fa = x
    while x > 1 :
        fa = fa*(x-1)
        x = x - 1
    return ( fa )

   

x = int (input ("lotafan adad ... : "))


print (f"factoriel barabar ast ba = {fact(x)}")
