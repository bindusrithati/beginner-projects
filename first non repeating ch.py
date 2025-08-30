word = input("Enter the word: ")  # madhumathi
for i in word:#m
    count = 0
    for j in word:
        if i == j:
            count += 1
    if count == 1:
        print("The first non-repeating character is:", i)
        break
