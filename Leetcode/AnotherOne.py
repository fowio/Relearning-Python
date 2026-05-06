
class Movie():
    def __init__(self, title, year):
        self.title = title
        self.year = year
    def describe(self):
        return (f"{self.title} was released in {self.year}")
    def isOld(self):
        if self.year < 2000:
            return True
        else:
            return False
        
Matrix = Movie("Matrix", 1999)
Inception = Movie("Inception", 2010)
Interstellar = Movie("Interstellar", 2014)

print(Matrix.describe())
print(Matrix.isOld())

print(Inception.describe())
print(Inception.isOld())

print(Interstellar.desccibe())
print(Interstellar.isOld())

