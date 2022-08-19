num=[11,1,13,14,16,10]
a=[]
i=0
while i<len(num):
    if (num[i]>11):
        a.append(num[i])
    i=i+1
a.insert(0,-1)
a.insert(4,-1)
print(a)