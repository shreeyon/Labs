#4. Write a program to count the number of each character in a given string using a dictionary.
a=input("Enter a string: ")
count={}
for char in a:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(count)