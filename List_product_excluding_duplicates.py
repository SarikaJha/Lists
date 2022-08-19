list=[6,1,3,5,6,3,1]
a=[]
product=1
i=0
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
        product=product*a[i]
    i=i+1
print(product)