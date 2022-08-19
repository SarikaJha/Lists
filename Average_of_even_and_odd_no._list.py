elements=[23,14,56,12,19,9,15,25,31,42,43]
even=0
odd=0
even_sum=0
odd_sum=0
even_avg=0
odd_avg=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        even=even+1
        even_sum=even_sum+elements[i]
        even_avg=even_sum/even
    else:
        odd=odd+1
        odd_sum=odd_sum+elements[i]
        odd_avg=odd_sum/odd
    i=i+1
print("average of even numbers is:",even_avg)
print("average of odd numbers is:",odd_avg)