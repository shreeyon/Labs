#9. Write a program that finds all numbers between 100 and 999 where the sumn of the cubes of
#  the digits equals the number itself (Armstrong numbers).
print("Armstrong number between 100 and 999 are: ")
for i in range(100,1000):
    x=i//100
    y=(i//10)%10
    z=i%10
    if(x**3+y**3+z**3)==i:
        print(i)