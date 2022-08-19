#Write a Python program to convert a pair of values into a sorted unique array.
# list=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# a = []
# for x in list:
#     for y in x:
#         if y not in a:
#             a.append(y)
# print(a)


#Write a Python program to compute the difference between two lists. Go to the editor
#Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
#Expected Output:
#Color1-Color2: ['white', 'orange', 'red']
#Color2-Color1: ['black', 'yellow']
# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]
# a = []
# for color in color1:
#     if color not in color2:
#         a.append(color)
# print(a)

# b = []
# for color in color2:
#     if color not in color1:
#         b.append(color)
# print(b)


color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
colors=color1+color2
repe=[]
for a in colors:
    if a in repe:
        color1.remove(a)
        color2.remove(a)
    else: 
        repe.append(a)

print("color1-color2: ",color1)
print("color2-color1: ",color2)