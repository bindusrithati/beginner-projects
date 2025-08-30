a=input("enter numbers:")
b=a.split(" ")
b=[int(x) for x in b]
max_num=b[0]
for i in b:
    if i>max_num:
        max_num=i
print(max_num)