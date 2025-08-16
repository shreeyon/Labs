class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
   
    def show_details(self):
        print("Name=",self.name)
        print("Marks=",self.marks)

s1=Student("Shriyon Nepal",97.2)
s1.show_details()
s2=Student("Binupa Dhunagan",98)
s2.show_details()
s3=Student("Min Bahadur Gurung",88)
s3.show_details()