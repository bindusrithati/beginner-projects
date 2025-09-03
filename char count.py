input = input("enter a word:")
fre = {}
for i in input:
    if i in fre:
        fre[i]+=1
    else:
        fre[i] = 1
print("the frequency of each character is :", fre)