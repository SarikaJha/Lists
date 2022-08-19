a=[5,"6",9.8,"moni",4,"6"]
i=0
sum=0
while i<len(a):
    if (type(a[i])==int):
        sum=sum+a[i]
    i=i+1
print(sum)