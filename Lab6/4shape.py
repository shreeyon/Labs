class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
            return self.length*self.breadth
    
class Circle(Shape):
    def __init__(self,radius):
       self.radius=radius
    def area(self):
            return (22/7)*self.radius**2
shapes=[Rectangle(10,6),Circle(7)]
for s in shapes:
    print("Area=",s.area())

    