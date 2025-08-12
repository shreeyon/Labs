#6. Write a program that accepts 10 integers from the user and counts how many are positive, negative, and zero.
a=[]
for i in range(0,10):
    num=int(input(f"Enter a number {i+1} : "))
    a.append(num)
ctp=0 
ctn=0
ctz=0
for item in a:
    if(item>0):
        ctp=ctp+1
    elif(item==0):
        ctz=ctz+1
    else:
        ctn=ctn+1
print(f"Positive numbers : {ctp}\nNegative numbers : {ctn}\n Zero number : {ctz}")