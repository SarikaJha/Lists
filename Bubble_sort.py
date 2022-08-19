a=[5,3,56,8,9,23,6]
j=0
while j<len(a):
    i=0
    while i<len(a)-1:
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
        i+=1
    j+=1
print(a)