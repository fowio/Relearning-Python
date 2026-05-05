
width = int(input("What is the width of the rectangle?: "))
height = int(input("What is the height of the rectangle?: "))
symbol = input("Enter your symbol: ")
gap = int(width - 2)

selection = input("Which version do you want? (Enter for Mine): ")
# for column in range(0, height):
#     for rows in range(0, width):
#         print(f"{symbol}", end="")
#     print()

if selection == "":
    for rows in range (0, width):
        if rows == 0 or rows == height-1:
            for printw in range(0, width):
                print(f"{symbol}", end="")
            print()
            if rows == height-1:
                break    
        else:
            print(f"{symbol}", end="")
            for gaps in range(0, gap):
                print(" ", end="")
            print(f"{symbol}")

else: # Claude's :(
    for row in range(height):
        if row == 0 or row == height - 1:
            print(symbol * width)
        else:
            print(symbol + " " * gap + symbol)
