numbers=[62,40,23,70,56,12,5,10,7]
# numbers.sort()
# print("the second max number is =",numbers[-2])
i=0
while i<len(numbers):
    j=0
    while j<len(numbers):
        if numbers[i]<numbers[j]:
            a=numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=a
        j+=1
    i+=1
print("second max:",a)