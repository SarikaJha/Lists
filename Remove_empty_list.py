list=[5,6,[],3,[],[],9]
i=0
a=[]
while i<len(list):
    if (type (list[i])==int):
        a.append(list[i])
    i=i+1
print(a)