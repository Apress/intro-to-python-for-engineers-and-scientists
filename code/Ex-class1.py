#Python code to show usage of __init__

# Defining a class "library"
# which stores information about book's name and price

#Defining class
class library:
   'The base class for all books'
   bookCount = 0 #Class variable setting count of books to zero

   def __init__(self, name, price):# Initializing the instance of class with name, price and updated book count
      self.name = name
      self.price = price
      library.bookCount += 1
   
   def displayCount(self):
     print("Total Employee %d",library.bookCount)

   def displayBook(self):
      print("Name : ", self.name,  ", Price: ", self.price)

#Creating objects

book1 = library("Introduction to python",100) # First instance of object "library"
print(type(book1))

book2 = library("Basic Python",150) # Second instance of object "library"
print(type(book2))

book3 = library("Intermediate Python",200) # Third instance of object "library"
print(type(book3))

book4 = library("Advanced Python",300) # Four instance of object "library"
print(type(book2))

# Accessing attributes

print("Details of first book:")
book1.displayBook()

print("Details of second book:")
book2.displayBook()

print("Details of third book:") 
book3.displayBook()

print("Details of fourth book:")
book4.displayBook()

print("Total Number of books= %d" % library.bookCount)

# Probing the bult-in attributes

print("library.__doc__:", library.__doc__)
print("library.__name__:", library.__name__)
print("library.__module__:", library.__module__)
print("library.__bases__:", library.__bases__)
print("library.__dict__:", library.__dict__)
