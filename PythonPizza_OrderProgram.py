class Pizza:
    def __init__(self):
        self.size = price
        self.pepperoni = fee
        self.cheese = add

    def bill(self):
        print(f"Your final bill is: ${self.size + self.pepperoni + self.cheese}")


while True:
    print("Small - $15, Medium - $20, Large - $25")
    size = input("What size of pizza do you want? (S, M, L): ").lower()
    print(" ")
    if size == "s":
        price = 15
        break
    elif size == "m":
        price = 20
        break
    elif size == "l":
        price = 25
        break
    else:
        print("Select a correct pizza size. S, M or L")

while True:
    print("Pepperoni for small: +$1, Pepperoni for medium/large: +$2")
    add_pepperoni = input("Do you want to add pepperoni? (Yes or No): ").lower()
    print(" ")
    if size == "s":
        if add_pepperoni == "yes":
            fee = 1
            break
        elif add_pepperoni == "no":
            fee = 0
            break
        else:
            print("Invalid input. To add pepperoni, select Yes or No")
    elif size == "m":
        if add_pepperoni == "yes":
            fee = 2
            break
        elif add_pepperoni == "no":
            fee = 0
            break
        else:
            print("Invalid input. To add pepperoni, select Yes or No")
    elif size == "l":
        if add_pepperoni == "yes":
            fee = 2
            break
        elif add_pepperoni == "no":
            fee = 0
            break
        else:
            print("Invalid input. To add pepperoni, select Yes or No")

while True:
    print("Extra cheese: +$1")
    extra_cheese = input("Do you want extra cheese? (Y/N): ").lower()
    print(" ")
    if size == "s":
        if extra_cheese == "y":
            add = 1
            break
        elif extra_cheese == "n":
            add = 0
            break
        else:
            print("Invalid input. To add extra cheese, select Y/N")
    elif size == "m":
        if extra_cheese == "y":
            add = 1
            break
        elif extra_cheese == "n":
            add = 0
            break
        else:
            print("Invalid input. To add extra cheese, select Y/N")
    elif size == "l":
        if extra_cheese == "y":
            add = 1
            break
        elif extra_cheese == "n":
            add = 0
            break
        else:
            print("Invalid input. To add extra cheese, select Y/N")


my_pizza = Pizza()
my_pizza.bill()
