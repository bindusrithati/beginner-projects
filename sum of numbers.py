a = (input("enter the number:"))
b=a.split(" ")
b=[int(x) for x in b]
sum=0
for i in b:
    sum+=i
print("the sum is:", sum)
