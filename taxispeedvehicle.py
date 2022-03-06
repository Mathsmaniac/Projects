import random


def triplength():
    while True:
        try:
            length = int(input("\nHow long was the trip? "))
        except ValueError:
            print("please type a number")
        else:
            break
    price = 10 + length * 2
    print(f"The price for your trip is ${price:.2f}")
    return price


def speedask():
    speedy = ""
    fine = 0
    if random.randint(1, 3) == 3:
        print("You were caught speeding! ")
        print("(For police to fill out)")
        while True:
            try:
                speedy = int(input("How fast over the speed limit? "))
            except ValueError:
                print("Please type a number")
                continue
            if speedy <= 0:
                print("Why did you pull them over if they weren't speeding?")
                return 0
            else:
                break
        keys_list = list(fines)
        for item in keys_list:
            if speedy <= item:
                fine = fines[keys_list[keys_list.index(item)-1]]
                break
            else:
                fine = 630
        print(f"The fine is ${fine:.2f}")
        return fine
    else:
        print("You didn't speed, nice")
        return 0


def getcar(number):
    foo = 0
    options = []
    for key, value in vehicles.items():
        value = value[1]
        if value == number:
            print(f"For {vehicles[key][0]}, type {key}")
            options.append(key)
            foo = 1
        if value >= number and foo == 0:
            print(f"We don't have the car you're looking for, but the next best option is {vehicles[key][0]}, with {vehicles[key][1]} seats, for this one, type {key}")
            options.append(key)
            foo = 1
    if foo == 0:
        print("We don't have a car with that many, or a greater amount of seats, sorry")
        return None
    else:
        while True:
            try:
                car = int(input("Which car would you like? "))
            except ValueError:
                print("Please enter a number")
                continue
            if car in options:
                return car
            else:
                print("That number is not an option")


fines = {1: 30, 10: 80, 15: 120, 20: 170, 25: 230, 30: 300, 35: 400, 40: 510, 45: 630}
summary_stats = {}
vehicles = {1: ["Suzuki Van", 2], 2: ["Toyota Corolla", 4], 3: ["Honda CRV", 4], 4: ["Suzuki Swift", 4], 5: ["Mitsubishi Airtrek", 4], 6: ["Nissan DC Ute", 4], 7: ["Toyota Previa", 7], 8: ["Toyota Hi Ace", 12], 9: ["Toyota Hi Ace", 12], }
while True:
    if input("\nStart a new trip? Type 'yes' to start or anything else to not: ").lower() == 'yes':
        while True:
            name = input("What is your name? ")
            if name in summary_stats:
                print("Please change that name")
            else:
                break
        if name.lower() == "james wilson" or name.lower() == "helga norman" or name.lower() == "zachary conroy":
            print("You are wanted for arrest, we still want your money so we won't tell anyone")
        while True:
            try:
                seats = int(input("\nHow many seats would you like in your taxi ? "))
            except ValueError:
                print("Please enter a number")
            else:
                broom = getcar(seats)
                try:
                    broombroom = vehicles.pop(broom)[0]
                except KeyError:
                    continue
                else:
                    break
        speedyness = triplength()
        fine = speedask()
        summary_stats[name] = [broombroom, speedyness, fine]
    else:
        break
print("Over the course of the day: ")
for thingy in summary_stats:
    print(f"{thingy} caught a {summary_stats[thingy][0]} taxi, costing ${summary_stats[thingy][1]:.2f} for the time he spent in it. He was fined ${summary_stats[thingy][2]:.2f} for speeding")
