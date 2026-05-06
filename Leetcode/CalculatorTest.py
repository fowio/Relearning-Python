
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    
Number1 = int(input("a: "))
Number2 = int(input("b: "))

myCalc = Calculator()

print(myCalc.add(Number1,Number2))
print(myCalc.subtract(Number1,Number2))
