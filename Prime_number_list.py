n=int(input("enter the number:"))
count=0
i=2
while i<=n//2:
    if n%i==0:
        count=count+1
        break
    i=i+1
if count==0:
    print("Your number is a prime number!")
else:
    print("Your number is not a prime number!")