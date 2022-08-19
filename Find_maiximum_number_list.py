num=int(input("enter the number:"))
i=0
a=[]
while i<num:
    list=int(input("enter the list:"))
    a.append(list)
    i=i+1
print("first max:",max(a))
print("second max:",a[-2])
print("third max:",a[-3])