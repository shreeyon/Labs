#3. Write a program that reads a number and prints the factorial of that number using a while loop.
a=int(input("Enter a number "))
fact=1
i = 1
while (i<=a):
    fact=fact*i
    i=i+1
print(f'The factorial of {a} is {fact}')
