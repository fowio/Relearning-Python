
Username = input("Enter your desired username (1-12 Char): ")

if len(Username) > 12:
    print("Sorry, it must contain less than 12 characters")
elif Username.count(" ") > 1:
    print("Sorry, your username cannot contain spaces.")
elif Username.isalpha() == False:
    print("Sorry, your username must not contain digits and symbols.")
else:
    print(f"Hello, {Username}!")