#You will be given a number and you need to return it as a string in Expanded Form.
num=int(input("number"))
a= []
i = len(str(num)) -1
for s in str(num):
    if s != "0":
        a.append(s + "0" * i)
    i -= 1
print(" + ".join(a))