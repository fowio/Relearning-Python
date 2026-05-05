# Is a loop embedded in that loop, O(n squared)
for x in range(3):
    for y in range(1,10): #counts 1 to 9
        print(y, end= "")
    print() # new line