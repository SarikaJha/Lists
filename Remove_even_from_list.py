##Write a Python program to print the numbers of a specified list after removing even numbers from it.
list=[12,3,6,8,9,10,11,13,15]
i=0
a=[]
b=[]
while i<len(list):
    if list[i]%2==0:
        a.append(list[i])
    else:
        b.append(list[i])
    i=i+1
print(b) 