class Animal:
    
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d1=Dog()
d1.speak()

