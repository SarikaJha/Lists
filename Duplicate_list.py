n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
a=[]
b=[]
i=0
while i<len(n):
    if n[i] not in a:
        a.append(n[i])
    else:
        if n[i] not in b:
            b.append(n[i])
    i=i+1
print(b)


# n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# a=[]
# b=[]
# duplicates=[]
# for i in n:
#     if i not in a:
#         a.append(i)
#     else:
#         b.append(i)
#         j=0
#         while j<len(b):
#             if b[j] not in duplicates:
#                 duplicates.append(b[j])
#             j+=1
# print(duplicates)