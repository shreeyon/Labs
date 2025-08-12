# 5. Create a function sum_numbers(*args) that accepts any number of numeric arguments and returns
# their sum.Test it with 2, 3, and 5 numbers.
def sum_number(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
sum_number(3,6)
sum_number(2,4,6)
sum_number(12,4,2,7,3)

   
 