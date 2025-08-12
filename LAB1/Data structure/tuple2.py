#2. Create a tuple of 10 integers. Write a program to display the maximum and minimum numbers from the tuple.
import random
a=tuple(random.randint(1,100) for _ in range(10))
largest=max(a)
smallest=min(a)
print(a )
print(f"Largest: {largest}\nSmallest is: {smallest}")