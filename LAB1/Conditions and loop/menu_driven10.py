#10.Write a menu-driven program to perform arithmetic operations (+, -, *, /)
#based on user choice using conditional statements.

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
ch=input("Enter the operator (+, -, *, /): ")
if(ch=='+'):
    print(a+b)
elif(ch=='-'):
    print(a-b)
elif(ch=='*'):
    print(a*b)
elif(ch=='/'):
    print(a/b)
else:
    print("Invaid operator")