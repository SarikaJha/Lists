# num=int(input("enter the required number"))
# n=[]
# for i in range(num):
#     i=int(input("enter the number"))
#     n.append(i)
# print(n)
# print("value of maximum is",max(n))
# print("value of manimum is",min(n))


num=int(input("enter the required number:"))
n=[]
for i in range(num):
    i=int(input("enter the number:"))
    n.append(i)
j=0
max=n[0]
min=n[0]
while j<len(n):
    if n[j]>max:
        max=n[j]
    if n[j]<min:
        min=n[j]
    j+=1
print(max)
print(min)
