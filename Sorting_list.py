##Ascending
a=[1,2,13,4,21]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    i=i+1
print(a)

##Reverse
# a=[12,21,1,4]
# i=-1
# while i>=-len(a):
#     print(a[i],end=" ")
#     i=i-1