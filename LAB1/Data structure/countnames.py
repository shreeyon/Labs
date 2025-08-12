#8. Given a list of names, write a program to count how many times each name appears using a dictionary.
a=int(input("How many names do you want to add: "))
l=[]
for i in range(a):
    names=input("Enter a name: ")
    l.append(names)
count={}
for name in l:
    if name in count:
        count[name]+=1
    else:
        count[name]=1
print(count)