temp = 2
is_sunny = False

if temp >=28 and is_sunny:
    print("It is hot outside")
    print("It is sunny!")
elif temp <= 0 and is_sunny:
    print("It is cold outside!")
    print("And it is Sunny!")
elif temp in range(0, 29) and is_sunny:
    print("It is warm and sunny outside")
elif temp >=28 and not is_sunny:
    print("It is hot outside")
    print("It isn't sunny!")
elif temp <= 0 and not is_sunny:
    print("It is cold outside!")
    print("And it isn't Sunny!")
elif temp in range(0, 29) and not is_sunny:
    print("It is warm and not sunny outside")