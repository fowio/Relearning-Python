
# Exercise about Lists

print("Hello! Welcome to our Store")
print("Here are our items and their prices!")

items = ["apples", "oranges", "bananas", "spinach"]
prices = [2.99, 1.99, 4.99, 3.99]

print()
print("item" + "       " + "price")
print()
 
counter = 0
total = 0
for i in range(0,len(items)):
    print(items[i] + "     " + str(prices[i]))

select = input("Select an item? (Y/N): ")

while select.lower() == "y":
    choice = int(input(f"Select your item! (1 to {4-counter}): ")) - 1
    counter += 1

    total += prices[choice]
    print()
    print(f"You have selected {items[choice]}!")
    print(f"The total price is: {total}")

    prices.pop(choice)
    items.pop(choice)
    
    print()
    print("item" + "       " + "price")
    print()
    

    for i in range(0,len(items)):
        print(items[i] + "     " + str(prices[i]))

    select = "n"
    print()
    select = input("Select another item? (Y/N): ")

print(f"Your total is ${total}! Have fun using them!")
