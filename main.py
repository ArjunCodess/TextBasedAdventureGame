import time

def print_slow(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()

def living_room():
    print("You enter the living room.")
    print_slow("As you walk in, you see a sleeping pitbull guarding some gold jewelry.")
    print("Do you want to steal the jewelry from the pitbull? (yes/no)")

    pitBullChoice = input("> ")

    if pitBullChoice == "yes":
        print_slow("You attempt to steal the jewelry, but the pitbull wakes up and rips you to shreds.")
        print("You are now dead.")
    elif pitBullChoice == "no":
        print("You decide not to steal the dog's jewelry.")
        print_slow("As you turn around, you hear a faint sound coming from behind the sofa.")
        print_slow("You find a hidden passage leading to another room.")
        time.sleep(1)
        return "secret_room"
    else:
        print("Invalid choice. Please enter yes or no.")
        return living_room()

def dining_room():
    print("You chose to go into the dining room.")
    print_slow("As you walk in, you see a shiny vase on the table.")
    print("Do you want to open the vase? (yes/no)")

    vaseChoice = input("> ")

    if vaseChoice == "yes":
        print_slow("You open the vase and find a pile of bones!")
        time.sleep(1)
        return "secret_room"
    elif vaseChoice == "no":
        print("You decide not to open the shiny vase.")
        print_slow("As you turn to leave, you hear a cracking sound coming from the corner.")
        print_slow("A dark figure with glowing red eyes launches at you, knocking you unconscious.")
        print_slow("You wake up in your bed. It was all a dream.")
        time.sleep(1)
        return "exit"
    else:
        print("Invalid choice. Please enter yes or no.")
        return dining_room()

def secret_room():
    print("You find yourself in a mysterious secret room.")
    print_slow("You see a dusty bookshelf with a strange-looking book.")
    print("Do you want to take the book with you? (yes/no)")

    bookChoice = input("> ")

    if bookChoice == "yes":
        print_slow("As you take the book, the room starts to tremble, and the bookshelf reveals a hidden passage.")
        print_slow("You walk through the passage and find a chest full of valuable gems!")
        print_slow("Congratulations! You've found a treasure!")
        time.sleep(1)
        return "exit"
    elif bookChoice == "no":
        print("You decide not to take the mysterious book.")
        print_slow("As you turn around, the hidden passage behind the bookshelf closes.")
        time.sleep(1)
        return "exit"
    else:
        print("Invalid choice. Please enter yes or no.")
        return secret_room()

def main():
    print("Welcome to the Creepy Castle!")
    print("You are a distant family member of a rich millionaire who has just passed away, leaving this mansion to you.")
    print("As the newfound owner, you decide to pay a visit to the mansion.")
    print("The house is dated, creaky, and falling apart. You walk in the front door.")
    print("Do you want to enter the living room or the dining room?")

    roomChoice = input("> ").lower()

    if roomChoice == "living room":
        next_room = living_room()
    elif roomChoice == "dining room":
        next_room = dining_room()
    else:
        print("Invalid choice. Please enter living room or dining room.")
        return

    while next_room != "exit":
        if next_room == "secret_room":
            next_room = secret_room()

    print_slow("You've decided to leave the creepy castle. Goodbye!")

if __name__ == "__main__":
    main()
  
