class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll=roll_number
        self.marks=marks

    def display_info(self):
        print(f"Name={self.name}\nRoll_Number={self.roll}\nMarks={self.marks}")

s1=Student("Ram",12,88)
s1.display_info()


