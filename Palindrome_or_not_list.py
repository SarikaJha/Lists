# string=input("enter the string:")
# list1=list(string)
# length=len(list1)
# i=-1
# n=[]
# while i>=-length:
#     n.append(list1[i])
#     i=i-1
# if n==list1:
#     print(n,"is palindrome")
# else:
#     print(n,"is not palindrome")
# print(list1)
# print(n)


string=input("enter the string:")
rev_string=string[::-1]
print("reverse string:",rev_string)
if string==rev_string:
    print("string is a palindrome")
else:
    print("string is not palindrome")