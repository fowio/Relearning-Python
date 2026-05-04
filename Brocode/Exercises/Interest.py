
# Interest Calculator

# I will add a choice to see my previous coding attempt before the tutorial:

choice = input("Do you want to see the first section? Enter for YES: ")

# The formula given is A = P x (1 + r/n)^t

while choice == "":
    P = input("What is your initial balance?: ")

    # Validating the input..!
    while not P.isnumeric() or int(P)<=0:
        print("Invalid amount!")
        P = input("What is your initial balance?: ")
    
    r = input("What is the annual interest rate? (%): ")

    # Copying from the above:
    while not r.isnumeric() or int(r)<=0:
        print("Invalid amount!")
        r = input("What is the annual interest rate?: ")

    t = input("How many years will the account stay open?: ")
    # Copying from the above:
    while not t.isnumeric() or int(t)<=0:
        print("Invalid amount!")
        t = input("How many years?: ")

    # Forgot to int() them, the fix issss:
    # No, actually they are all floats
    P = float(P)
    r = float(r)
    t = float(t)

    A = P*(1+(r/100))**t

    print()
    print(f"Your money after {t} years will be: ${A:,.2f}")
    print(f"Happy banking!")
    break

# BroCode's:
while not choice == "":

    principle = 0
    rate = 0
    time = 0

    # wow this is shorter than what I came up with
    # might have to change it

    while principle <= 0:
        principle = float(input("Enter the principle amount: "))
        if principle <= 0:
            print("Principle can't be less than or equal 0!")

    while rate <= 0:
        rate = float(input("Enter the interest rate: "))
        if rate <= 0:
            print("Interest rate can't be less than or equal 0!")

    while time <= 0:
        time = int(input("Enter the time in years: "))
        if time <= 0:
            print("Time can't be less than or equal 0!")

    print(principle)
    print(rate)
    print(time)

    # Oh he has the formatting as well, hehe

    total = principle * pow((1 + rate/100), time)
    print(f"Balance after {time} year(s): ${total:.2f}")

    break