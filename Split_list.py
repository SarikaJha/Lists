##Write a Python program to split a list every Nth element.
##Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
##Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
# b,c,d =[],[],[]
# for i in a:
#     if a.index(i)%3==0:
#         b.append(i)
#     elif a.index(i)%3==1:
#         c.append(i)
#     elif a.index(i)%3==2:
#         d.append(i)
# print([b,c,d])


list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
a=[]
i=0
while i<len(list):
    i=i+1
a.append(list[0::3])
a.append(list[1::3])
a.append(list[2::3])
print(a)