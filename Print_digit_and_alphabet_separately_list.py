list=["A",1,2,3,"B","C"]
a=[]
b=[]
i=0
while i<len(list):
    if list[i] not in a and str(list[i]).isdigit():
        a.append(list[i])
    else:
        if list[i] not in a:
            b.append(list[i])
    i=i+1
print(a)
print(b)