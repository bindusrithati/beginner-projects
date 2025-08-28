a=int(input("enter a number:"))
b=int(input("enter a number:"))
if a==0 or 1:
    print("they are not primes")
for i in range(a,b):
    no_of_times=0
    for j in range(2,i):
        if i%j==0:
            no_of_times=1
    if no_of_times==0:
        print(i)
