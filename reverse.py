input = input("enter a sentence:")
words=[]
word=""
for i in input:
    if i!=" ":
        word+=i
    else:
        words.append(word)
        word=""
words.append(word)
for j in words:
    rev_str=""
    for h in j:
        rev_str=h+rev_str
    print(rev_str,end=" ") 