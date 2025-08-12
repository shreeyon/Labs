class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display_info(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Price:{self.price}")

    def update_price(self,new_price):
        self.price=new_price
        print(f"The price of the book is now updated to {self.price}")

book1=Book("Python Book","Guido van Rossum","400")
book1.display_info()
book1.update_price(500)
book1.display_info()