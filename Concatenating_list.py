#Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
#Sample list : ['p', 'q']
#n =5
#Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
list=['p','q']
a=[]
n=5
i=1
while i<=5:
    j=0
    while j<len(list):
        k=str(i)
        b=list[j]+k
        a.append(b)
        j+=1
    i+=1
print(a)