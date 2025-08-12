#7. Write a Python program to merge two dictionaries and sum the values of common keys.
d1={'a':10,'b':4}
d2={'a':5,'b':6,'c':17}
for k,v in d1.items():
    if k in d2.keys():
        d2[k]=d2[k]+v
    else:
        d2[k]=v
print(d2)