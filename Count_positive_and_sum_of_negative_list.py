list=[0,2,3,0,5,6,7,8,9,10,-11,-12,-13,-14]
i=0
positive=0
negative=0
sum=0
count=0
b=[]
while i<len(list):
    if list[i]>0:
        positive+=1
        count+=1
    elif list[i]<0:
        negative+=1
        sum=sum+list[i]
    else:
        pass
    i=i+1
b.append(count)
b.append(sum)
print(b)