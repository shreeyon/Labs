class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id=employee_id
        self.salary=salary
    def display(self):
        print(f"Name={self.name}\nAge={self.age}\nEmployee_ID={self.employee_id}\nSalary={self.salary}")
e1=Employee("Shriyon",19,123,50000)
e1.display()
