list1 = [1,7,8,6,7,8,4,3,2]
unique = {}
for i in list1:
    if i in unique:
        unique[i]+= 1
    else:
        unique[i]=1
list2=[key for key,value in unique.items() if value==1]
print(list2)
