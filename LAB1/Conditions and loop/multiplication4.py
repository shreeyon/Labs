#4. Write a program to print the multiplication table of a given number using a for loop.
a=int(input("Enter a number"))
for i in range(1,11):
    mul=a*i
    print(f'{a}*{i}={mul}')    