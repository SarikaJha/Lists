#Write a Python program to find the list of words that are longer than n from a given list of words.
list=["abc","kiram","python","xyz"]
word_len=[]
n=3
for i in list:
    if len(i)>n:
        word_len.append(i)
print(word_len)