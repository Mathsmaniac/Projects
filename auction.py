import random


def showmoney(apple):
    print("Your current balance is ${:.2f}".format(players.get(apple)))


# main
print("-------------------------------------------------------------")
print("Hello, welcome to the auction game!")
if input("Press 'Y' to view full instructions, otherwise type a"
         "nything else: ").lower() == 'y':
    print("\nYou and any amount of players will bid for a secretly val"
          "ued item items are valued between 30 and 1000 dollars")
    print("Each player starts with $1000")
    print("It takes $20 to enter the bid")
    print("Each player takes turns bidding on each item, when you don't want t"
          "o bid anymore, simply type 'out', you'll be back in the next "
          "round.")
    print("If you do not have enough to raise the bid, you will automatically"
          " exit this round of bidding")
    print("When someone wins the bid by everyone else exiting the bid, the"
          " value of the item will be revealed.")
    print("This players balance will then decrease by the amount they bid for "
          "the item, and increase by the value of the item")
    print("Players are taken out by either being bankrupt by having negative "
          "money,")
    print("quitting while they're ahead, players can quit at the end of an auction,")
    print("or not having enough money to enter the next bid")
    print("At any time on your turn, you can type 'view' to see how much money"
          " you have")
print("Let's begin!")
print("-------------------------------------------------------------")
STARTBID = 30
players = {}
outser = 0
while True:
    playernum = input("How many people are playing?"
                      " There have to be more than 1: ")
    try:
        playernum = int(playernum)
    except ValueError:
        print("Please type a number")
        continue
    if playernum < 2:
        print("There can't be less than two players")
    else:
        break
for i in range(playernum):
    while True:
        name = input("What is your player name? ")
        if name in players:
            print("There is already someone of that name playing, plea"
                  "se choose a different name")
        else:
            players[name] = 600
            break
while len(players) > 1:
    playingplayers = []
    for a in players:
        playingplayers.append(a)
    random.shuffle(playingplayers)
    sellthing = input("What is for sale? ")
    sellprice = random.randint(30, 1000)
    if random.randint(1, 300) == 250:
        sellprice = 10000000
    print("Starting bid is $30")
    currentbid = STARTBID
    otherplayers = playingplayers.copy()
    for a in playingplayers:
        players[a] -= 20
    while True:
        playingplayers = otherplayers.copy()
        for person in playingplayers:
            if len(otherplayers) < 2:
                break
            while True:
                bid = input(f"\nWhat would {person} like to bid? The current bid is at ${currentbid:.2f} ")
                if bid.lower() == 'view':
                    showmoney(person)
                    continue
                elif bid.lower() == 'out':
                    print(f"{person} is out!")
                    otherplayers.remove(person)
                    break
                try:
                    bid = int(bid)
                except ValueError:
                    print("Please enter a number, or 'view', or 'out'")
                    continue
                if bid > players.get(person):
                    print("you don't have enough money to make this bid")
                    continue
                if bid <= currentbid:
                    print("Please enter a number greater than the current bid")
                    continue
                else:
                    print(f"Bid successful! New bid is ${bid:.2f}")
                    currentbid = bid
                    break
            outs = []
            for individual in playingplayers:
                if players.get(individual) <= currentbid:
                    outs.append(individual)
            for item in outs:
                print(f"{item} is out of this bid due to not enough money")
                otherplayers.remove(item)
            if len(otherplayers) == 0:
                otherplayers.append(person)
        if len(playingplayers) < 2:
            break
    winner = playingplayers[0]
    print(f"End of the auction! {winner} has won!")
    print(f"The value of the item was ${sellprice:.2f}")
    money_won = sellprice - currentbid
    if abs(money_won) == money_won:
        print(f"\n{winner} has won ${money_won:.2f}")
    else:
        print(f"\n{winner} has lost ${abs(money_won):.2f}")
    players[winner] += money_won
    for person in players.copy():
        baz = input(f"{person}, type 'y' to quit the auction,"
                    f" or type anything else to stay: ").lower()
        if baz == 'view':
            showmoney(person)
        if baz == 'y':
            print(f"{person} has quit the auction with ${players.get(person):.2f} worth of various paraphernalia")
            players.pop(person)
print("The auction has finished!")

quit()
