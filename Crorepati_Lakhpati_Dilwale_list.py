money=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
a=[]
b=[]
c=[]
a1=0
b1=0
c1=0
i=0
while i<len(money):
    if money[i]>=100000000:
        a.append(money[i])
        a1+=1
    elif money[i]>=1000000:
        b.append(money[i])
        b1+=1
    else:
        if money[i]<1000000:
            c.append(money[i])
            c1+=1
    i=i+1
print(a1,"=","crorepati")
print(b1,"=","lakhpati")
print(c1,"=","dilwale")