
name = input("What is your name?: ")

while name == "": #Exists forever until it is FALSE
    print("You did not enter your name!")
    name = input("What is your name?: ") # Exit strategy

print(f"Hello, {name}!")

age = input("Enter your age: ")
 
while not age.isnumeric() or int(age) <= 0:
    print("You cant't do that!")
    age = input("Enter you age: ")

age = int(age)

# Before I learnt about isnumerical :(

# while age == "" or age.isalpha():
#     print("You can't do that! Enter your age:")
#     age = input("Enter your age: ")
#     age = age.replace(" ", "")

print(f"You are {age} years old!")
# -----------------------

# Example 3:

# food = input("Enter a food that you like! (q to quit): ")

# while not food == "q":
#     print(f"Yummy! You like {food}!")
#    food = input("Another one? q to quit!: ")

# I am trying to figure out how to use indexing for it:

food = [] # Forgot that an Array/List is [] (was 0)

# My sad attempt below

# i = 0
# while i >= 0: # until user quits
#    food[i] = input("Enter a food you like!: ")
#    while food[i].lower() != "q":
#       i += 1 # Previously i += i
#        food[i] = input("Another one? Q to quit: ")
#    break
#
#print("The foods you like includes: ")
#while i >= 0:
#    print(food[i])
#    if food[i] == "q":
#        break

while True:
    entry = input("Enter a food you like! (Q to quit): ")
    if entry.lower() == "q":
        break
    food.append(entry) # Will look to see what does append do

print("The foods you like include:") # So Python uses Item instead of Indexing
for item in food:
    print(item)
