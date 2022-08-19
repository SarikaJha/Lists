list=[2,3,6,4,2,1]
index=0
total_sum=0
while index<len(list):
    total_sum=list[index] + total_sum
    index=index+1
print("sum =",total_sum)