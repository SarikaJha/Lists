##For example, if we give 9119  the function should return  811181, as the  square of 9 is 81 and square of 1  is 1.
a=[9119]
i=0
string=[]
while i<len(a):
    b=str(a[i])
    i=i+1
    j=0
    c=str(b)
    square=0
    while j<len(c):
        string.append(int(c[j]))
        square=string[j]*string[j]
        j=j+1
        print(square,end="")