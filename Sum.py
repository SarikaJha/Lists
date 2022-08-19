a=[2,4,"5",3,"8"]
i=0
sum=0
sum1=0
while i<len(a):
    if (type(a[i])==list):
        sum=sum+a[i]
    else:
        sum1=sum1+a[i]
    i+=1
print(sum+sum1)