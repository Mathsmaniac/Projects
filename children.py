def kidnap():
    while True:
        child = input("Please enter the name of the child you want to "
                      "kidnap\nif y"
                      "ou want two children kidnapped, please run this"
                      " twice: ")
        if child == '0':
            return
        if child in children:
            print("We are already holding a child of that name, to prevent "
                  "confusion please rename this child, for information on ho"
                  "w to do this visit: https://www.babycenter.com/0_how-to-ch"
                  "ange-your-childs-name_3641846.bc#:~:text=To%20change%20the%"
                  "20name%20on,without%20requiring%20a%20court%20order.")
        else:
            break
    while True:
        ransom = input("Please enter the ransom for this child: ")
        if ransom == '0':
            return
        try:
            ransom = int(ransom)
        except ValueError:
            print("Enter a number, not a word")
        else:
            break
    child = child.lower()
    children[child] = ransom


def pickup():
    while True:
        pick = input("Please enter the name of the child you wish to pick up: ")
        if pick == '0':
            return
        if pick in children:
            print(f"Child removed! The price is; {calcer(pick)}")
        children.pop(pick)
        break


def calc():
    while True:
        foo = input("\nWhat is the name of the child"
                    " you want to know the cost for? ")
        if foo == '0':
            return
        if foo in children:
            print(f"The price of the kid is: {calcer(foo)}")
            break
        else:
            print("That child is not currently being held by us, try again")


def calcer(childs):
    bar = children[childs]
    bar += bar/100
    bar = "${:,.2f}".format(bar)
    return bar


def showchild():
    foo = children.keys()
    if len(foo) == 0:
        print("No children being held captive yet")
    else:
        print(*children.keys(), sep=", ")


# main
children = {}
print("----------------------------------------")
print("Welcome to MGS Child Kidnapping service")
print("We kidnap a child of your choice and hold them for ransom")
print("The parent then comes and collects them for the ransom you set"
      "and a slice for us for holding them based on the price of your ransom,")
print("The more expensive the ransom, the more we charge for keeping them")
print("Note that at any time you can type '0' and will return to the menu")
print("----------------------------------------")

while True:
    print("\nWhat would you like to do?")
    print("\n1: Have a child kidnapped")
    print("2: Pick up your child")
    print("3: Calculate the cost for keeping the child including "
          "your ransom price")
    print("4: Display all children being kept at our facility")
    print("5: Exit")
    while True:
        try:
            choice = int(input("\nPlease type your valid choice here: "))
            print()
            if 0 < choice < 6:
                if choice == 1:
                    kidnap()
                elif choice == 2:
                    pickup()
                elif choice == 3:
                    calc()
                elif choice == 4:
                    showchild()
                else:
                    print("Goodbye!")
                    quit()
                break
        except ValueError:
            pass
