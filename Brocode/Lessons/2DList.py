supplies = ["pen", 'pencil', 'paper']
for i, supply in enumerate(supplies):
    print(f'Index {i} in supplies is {supply}')

name = ['Pete', 'John', 'Emily']
age = [10, 11, 12]

for n, a in zip(name,age):
    print(f"{n} is {a} years old.")