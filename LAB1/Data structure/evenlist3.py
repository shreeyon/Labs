#3. Write a Python function that accepts a list and returns a new list with only the even numbers from the original list.
a=int(input("How many numbers do you want to add"))
og_list=[]
for i in range(0,a):
    num=int(input(f"Enter a number {i+1}: "))
    og_list.append(num)
new_list=[]
for item in og_list:
    if(item%2==0):
        new_list.append(item)
print(f'Original list={og_list}\nEven number={new_list}')