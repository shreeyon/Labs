#9. Write a Python program to remove elements from a list that are also present in another list.
a=int(input("How many element do you want to add in list 1"))

l1=[]
l2=[]
for i in range(a):
    element_in_first=input(f"Enter {i+1} element : ")
    l1.append(element_in_first)
b=int(input("How many element do you want to add in list 2"))
for i in range(b):
    element_in_second=input(f"Enter {i+1} element : ")
    l2.append(element_in_second)
for item in l2:
    if item in l1:
        l1.remove(item)

print(l1)
