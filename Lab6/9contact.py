class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Address:
    def __init__(self,street,city,zipcode):
        self.street=street
        self.city=city
        self.zipcode=zipcode

class Contact:
    def __init__(self,person,address):
        self.person=person
        self.address=address
    def contact_details(self):
        print(f"Name={self.person.name}\nAge={self.person.age}\nStreet={self.address.street}\nCity={self.address.city}\nZipcode={self.address.zipcode}")

p1=Person("Shriyon",19)
a1=Address("Paknajol Street","Kathmandu",44700)
c=Contact(p1,a1)
c.contact_details()

