#8. Write a program that reads a number and prints whether it is a palindrome or not.
a = input("Enter a number: ")
rev = a[::-1]

if a == rev:
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")
