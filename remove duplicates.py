list1 = [6,7,7,8,9,5,4,2,1,3,5]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print("the list after removing duplicates:",list2)