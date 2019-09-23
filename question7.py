# ### Problem 7:
# Create the class Books with name, rating, genre, and author properties/attributes. Create a class method that will change the rating of the book. Outside of the class, create three objects of the class Book and put them in an array. Lastly, USING THE ARRAY print only the names of the books using any method we’ve learned in class.

class Books:
    def _init_(self, name, rating, genre, author): #you need to have two underscores on each side of init you only have one
        self.name = name
        self.rating = rating
        self.genre = genre
        self.author = author

    def changeRating(self,newRating):
        self.rating = newRating

book1 = Books("Programmng Python", 10, "Non-Fiction", "Kenn"): #these colons are causing an error
book2 = Books("Programmng JavaScript", 10, "Non-Fiction", "Kevin"):
book3 = Books("Programmng HTML", 10, "Non-Fiction", "Erin")

bookArray = [book1, book2, book3]
for eachBook in bookArray:
    print(eachBook.name()) #you don't need parenthesis at the end of name you only need to define that you are looking for name



    # //The function does not need a parameter. You need to get the name property. The code needs a colon at the end of it.