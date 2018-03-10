if bool("bacon"):
    print("Yes pleaseeee!")

if "bacon":
    print("Yes pleaseeee!")

deck = 49
if deck == 52:
    print("Let's play!")
else:
    print("Nooooo!")

if deck == 52:
    print("Pokerrrr!")
else:
    if deck > 52:
        print("Get a deck of 52 cards")
    else:
        print("Why play??")

# Another variant of if-else - Flat structure
if deck == 52:
    print("Pokerrrr!")
elif deck > 52:
    print("Get a deck of 52 cards!")
else:
    print("Why play??")

# While loops - Explicit is better
beer = 6
while beer != 0:
    print(beer)
    beer -= 1  # Augmented assignment shorthand for x = x - 1
    # While loops

# While loops - Implicit is un-pythonic
beer = 12
while beer:
    print(beer)
    beer -= 1  # Augmented assignment shorthand for x = x - 1

# Break
while True:
    response = input()
    if int(response) % 6 == 0:
        print("Response is divisible by 6")
        break
