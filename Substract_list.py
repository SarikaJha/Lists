a=[1,2,3,4,5,6]
i=0
d=[]
while i<len(a)-1:
    c=a[i+1]
    b=str(a[i]-c)
    # b=str(c-a[i])
    d.append(b)
    i=i+2
print(d)
