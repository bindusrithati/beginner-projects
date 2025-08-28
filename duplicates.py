a=[1,4,3,2,4,2,4,4,2,3,7,5,5,6,9,44]
unique_elements=[]
for i in a:
    count=0
    for j in a:
        if i==j:
            count+=1
    if count==1:
        unique_elements.append(i)
result=[]
for x in unique_elements:
    if x in result:
        pass
    else:
        result.append(x)
print(result)