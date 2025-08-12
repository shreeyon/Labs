#Write a Python function named greet_user that takes a user's name and prints:
def greet_user(first_name,Last_name):
    first_name=first_name.capitalize()
    Last_name=Last_name.capitalize()
    return first_name +" " +Last_name

a=input("Enter your first name:")
b=input("Enter your Last name:")
c=greet_user(a,b)
print(c)
