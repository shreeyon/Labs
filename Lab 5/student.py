class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def show_details(self):
        print(f"Name:{self.name}")
        print(f"Marks:{self.marks}")



s1=Student("Shreeyon",100)
s2=Student("Divyans",90)
s3=Student("Hemanta",80)

s1.show_details()
s2.show_details()
s3.show_details()