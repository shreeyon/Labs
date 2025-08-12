#1. Write a Python program to remove all duplicates from a list and print the unique elements.
a=int(input("Enter how many numbers of item do you want to add in list"))
l=[]
for i in range(0,a):
    item=input(f"Enter the item {i+1}")
    l.append(item)
print(l)
unique=set(l)
print(unique)