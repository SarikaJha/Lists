elements=[23,14,56,12,19,9,15,25,31,42,43]
count_even=0
count_odd=0
sum_even=0
sum_odd=0
avg_even=0
avg_odd=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        count_even=count_even+1
        sum_even=sum_even+elements[i]
        avg_even=sum_even/count_even
    else:
        count_odd=count_odd+1
        sum_odd=sum_odd+elements[i]
        avg_odd=sum_odd/count_odd
    i=i+1
print("count of even numbers:",count_even)
print("count of odd numbers:",count_odd)
print("count of all the numbers:",count_even+count_odd)
print("sum of even numbers:",sum_even)
print("sum of odd numbers",sum_odd)
print("sum of all the numbers:",sum_even+sum_odd)
print("average of even numbers",avg_even)
print("average of odd numbers",avg_odd)
print("average of all the numbers:",avg_even+avg_odd)  