input = input("enter a sentence:")
word_count=0
is_word=False
for i in input:
    if i!=" ":
        if not is_word:
           word_count+=1
        #    is_word=True
    else:
        is_word=False
print("no.of words in the given sentence is:",word_count)
letter_count=0
for j in input:
    if ("A"<=j>="Z") or ("a"<=j>="z"):
        letter_count+=1
print("no.of letters in the given sentence are:",letter_count)