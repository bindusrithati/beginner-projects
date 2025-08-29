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
# print(words)#['this', 'is', 'bindu']
rev_str=""
for j in words:#this #is
  rev_str=j+" "+rev_str 
print(rev_str)