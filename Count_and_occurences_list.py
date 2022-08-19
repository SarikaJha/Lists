list=['2','t','u','6','2','d','6','d','u','1','2']
a=input("enter the number:")
i=0
count=0
while i<len(list):
    if a==list[i]:
        count=count+1
    i=i+1
print(a,"have occured",count,"times in a given list")