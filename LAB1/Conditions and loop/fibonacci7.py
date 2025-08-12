#7. Write a program to generate the Fibonacci sequence up to n terms.
a=int(input("Enter the number of terms: "))
x=0
y=1
print(f"Fibonacci series upto {a} terms are:")
for i in range(a):
    print(x)
    temp=x
    x=y
    y=temp+y