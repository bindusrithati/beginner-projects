input = input("enter a sentence:")
word_count=0
is_word=False
for i in input:
    if i!=" ":
        if not is_word:
           word_count+=1
           is_word=True
    else:
        is_word=False
print("no.of words in the given sentence is:",word_count)
