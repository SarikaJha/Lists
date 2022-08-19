a=[1,2,4,5,7,9,11,12,15]
i=1
b=[]
while i<=15:
    j=0
    if i not in a:
        b.append(i)
        j=j+1
    i=i+1
print(b)

# a=[1,2,4,5,7,9,11]
# i=1
# while i<=11:
#     j=0
#     while j<len(a):
#         if i not in a:
#             a.append(i)
#             a.sort()
#         j=j+1
#         i=i+1
# print(a) 

# list=[1,2,4,8,9,10]
# i=1
# a=[]
# while i<len(list):
#     if i not in list:
#         a.append(list[i])
#     i=i+1
# print(a)