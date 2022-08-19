numbers=[121,3,5,100,34,89,2,5]
i=0
min=numbers[0]
while i<len(numbers):
    if numbers[i]<min:
        min=numbers[i]
    i+=1
print(min)