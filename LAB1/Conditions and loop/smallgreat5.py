#5. Write a program to find the largest and smallest number in a list entered by the user.
a = int(input("How many numbers do you want to enter? "))

number = []
for i in range(a):
    num = int(input(f"Enter number {i + 1}: "))
    number.append(num)

print(f'List is {number}')
print(f'Largest is {max(number)} and smallest is {min(number)}')
