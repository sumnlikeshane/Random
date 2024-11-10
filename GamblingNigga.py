import random

# Function to ask the player if they want to play or quit
def play_or_quit():
    a = input()
    if a == "q":
        print("Imagine being such a loser.")
        return False
    elif a == "p":
        return True
    else:
        print("Invalid input. Quitting game, u fckin dumass.")
        return False

# Function to check if the player has enough money to continue
def money_checker(money):
    return money > 0

# Dictionary of slot machine symbols
dic = {1: "💎", 2: "🍒", 3: "🍋"}

# Initial game setup
choice = True
count = 0

# Slot Machine Welcome Screen
print("#############################################")
print("#                                           #")
print("#   🎰   Welcome to the Slot Machine!   🎰  #")
print("#                                           #")
print("#############################################")
print("#                                           #")
print("#   💵  Each spin costs $100                #")
print("#   💰  Every win earns you $200            #")
print("#   🎲  Minimum Bet: $100                   #")
print("#                                           #")
print("#############################################")
print("#                                           #")
print("#         Good luck and spin to win!        #")
print("#                                           #")
print("#############################################")

# Get initial amount of money from the player
money = int(input("How much money u betting: "))
money_Checker = money >= 100

# Main game loop
while choice and money_Checker:
    print()

    # Deduct $100 per spin
    money -= 100

    # Randomly select three symbols for the slot machine
    f = dic.get(random.randint(1, 3))
    s = dic.get(random.randint(1, 3))
    t = dic.get(random.randint(1, 3))

    # Display the slot machine with the chosen symbols
    print()
    print("+---------------------------+")
    print("|       SLOT MACHINE        |")
    print("+---------------------------+")
    print("|        |        |         |")
    print(f"|   {f}   |   {s}   |   {t}    |")
    print("|        |        |         |")
    print("+---------------------------+")
    print("|      [SPIN TO WIN!]       |")
    print("+---------------------------+")
    print()

    # Check if the player has money to continue
    money_Checker = money_checker(money)

    if money_Checker:
        # Win condition if two symbols match
        if f == s:
            print("You win $200.")
            money += 200
            print("Play more, ull win more (p), or Quit and go home with less money (q)")
            choice = play_or_quit()

        # Lose condition
        else:
            print("You didn’t win (yet).")
            count += 1
            print("Spin Again (p), or Quit and not win money (q): ", end=" ")
            choice = play_or_quit()
    else:
        print("Quitting game.\nU broke af nigga.")
        break