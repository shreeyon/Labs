a = int(input("How many numbers do you want to add in the list: "))
l = []

if a <= 0:
    print("Cannot find the maximum and minimum of an empty list.")
else:
    for i in range(a):
        num = int(input(f"Enter number {i+1}: "))
        l.append(num)
    
    maximum = l[0]
    minimum = l[0]
    
    for i in range(1, a):
        if l[i] > maximum:
            maximum = l[i]
        if l[i] < minimum:
            minimum = l[i]
            
    print(f"Maximum: {maximum}\nMinimum: {minimum}")