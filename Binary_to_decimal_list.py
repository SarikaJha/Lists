binary_numbers=[1,0,0,1,1,0,1,1]
i=-1
power=0
sum=0
while i>=-(len(binary_numbers)):
    n=binary_numbers[i]*2**power
    sum=sum+n
    power=power+1
    i=i-1
print(sum)