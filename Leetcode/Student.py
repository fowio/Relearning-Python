
class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def passing(self):
        if self.grade >= 50:
            return True
        else:
            return False
    def info(self):
        return(f"{self.name} has a grade of {self.grade}")

test = Student("Min", 50)    

print(test.info())
print(test.passing())