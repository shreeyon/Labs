class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
         return self.a+other.a
    def __sub__(self,other):
         return self.a-other.a
    def __mul__(self,other):
         return self.a*other.a
    def __truediv__(self,other):
         return self.a/other.a
    def __floordiv__(self,other):
         return self.a//other.a
    def __mod__(self,other):
         return self.a%other.a
    def __pow__(self,other):
         return self.a**other.a
    def __eq__(self,other):
         return self.a==other.a
    def __ne__(self,other):
         return self.a!=other.a
    def __lt__(self,other):
         return self.a<other.a
    def __le__(self,other):
         return self.a<=other.a
    def __gt__(self,other):
         return self.a>other.a
    def __ge__(self,other):
         return self.a>=other.a
    def __str__(self):
         return str(self.a)
c1=A(7)
c2=A(2)
print(f"\nINPUT:")
print(f"c1 = {c1}\nc2 = {c2}")
print(f"\nOUTPUT:")
print(f"c1+c2 : {c1+c2}")
print(f"c1-c2 : {c1-c2}")
print(f"c1*c2 : {c1*c2}")
print(f"c1/c2 : {c1/c2}")
print(f"c1//c2 : {c1//c2}")
print(f"c1%c2 : {c1%c2}")
print(f"c1**c2 : {c1**c2}")
print(f"c1>c2 : {c1>c2}")
print(f"c1<c2 : {c1<c2}")
print(f"c1==c2 : {c1==c2}")
print(f"c1>=c2 : {c1>=c2}")
print(f"c1<=c2 : {c1<=c2}")
print(f"c1!=c2 : {c1!=c2}")