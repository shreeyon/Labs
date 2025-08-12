#5. Create a set of prime numbers less than 50. Write a program to check whether a given number exists in the set or not.
l=[]
for n in range(1,51):
    count=0
    for i in range(1,n+1):
        if (n%i)==0:
            count+=1

    if(count==2):
        l.append(n)


a=int(input("enter a number: "))
if a in l:
    print(f'{a} is in list')
else:
     print(f'{a} is not in list')