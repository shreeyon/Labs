# 3. Create a function power(base, exponent=2) that returns the result of base raised to the power of
# exponent.Demonstrate it with and without the exponent argument.

#without the exponent argument.
def power(base,exponent=2):
    z=base**exponent
    return z
a=int(input("Enter the base:"))
b=power(a)
print(f"The result of {a} raised to power 2 is {b}")


#with the exponent argument.
c=power(a,5)
print(f"The result of {a} raised to power 5 is {c}")

