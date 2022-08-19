#Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
#Sample list: [11, 33, 50]
#Expected Output: 113350
# a=[11,33,50]
# i=0
# while i<len(a):
#     print(a[i],end="")
#     i=i+1

# a=[11,33,50]
# i=0
# x=[]
# while i<len(a):
#     b=str(a[i])
#     c="".join(b)
#     d=int(c)
#     i+=1
#     print(d,end="")

# lst = [11, 33, 50]
# lst1 = []
# for x in lst:
#     lst1.append(str(x))
# print(int(''.join(lst1)))

list=[11,33,50]
i=0
a=[]
while i<len(list):
    a.append(str(i))
print(int("".join(a)))