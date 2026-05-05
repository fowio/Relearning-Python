
# A single variable used to store values

fruits = ["apples", "oranges", "bananas", "coconuts"]
# print(fruits[1])

new = input("A fruit you like?: ")
fruits.append(new)
#fruits.remove("apples")
#fruits.insert(0, "Mangoes")
#fruits.sort
#fruits.reverse()
#fruits.clear()
print(fruits.index(new))


# print(dir(fruits))
# print(help(fruits))

#print(len(fruits))

#print("apple" in fruits)
#fruits[0] = "pineapple"

for fruit in fruits:
   print(fruit)