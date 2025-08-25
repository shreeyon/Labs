# 9. Given a list [10, 15, 20, 25, 30], use filter() and a lambda function to extract numbers divisible by
# 10.
a=[10,15,20,25,30]
print("The original list is:")
print(a)
print(list(filter(lambda x:x%10==0,a)))