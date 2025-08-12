#6. Given two lists, write a program to find their intersection using sets.
l1=[]
l2=[]
a=int(input("How many element do you want to add in set 1: "))
for i in range(0,a):
    x=int(input(f'Enter a {i+1} number: '))
    l1.append(x)
b=int(input("How many element do you want to add in set 2: "))
for i in range(0,b):
    y=int(input(f'Enter a {i+1} number: '))
    l2.append(y)
s1=set(l1)
s2=set(l2)
s3=s1.intersection(s2)
print(s3)
