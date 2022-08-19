#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
i=0
while i<len(list):
    if i==0 or i==4 or i==5:
        list.pop(i)
    i+=1
print(list)