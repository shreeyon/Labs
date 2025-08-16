class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display_info(self):
        print("Title =",self.title)
        print("Author =",self.author)
        print("Price =",self.price)

    def update_price(self,new_price):
        self.new_price=new_price

b1=Book("Teen Ghumti","B.P. Koirala",1200)
b1.display_info()
b1.update_price(1000)
print("Updated price=",b1.new_price)
b1.display_info()