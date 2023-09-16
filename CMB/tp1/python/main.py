from numpy import random
import time

MIN_NUMBER = 1
MAX_NUMBER = 1000

def game():
    ''' The game in itself    
    '''
    # The random number to guess
    r = random.randint(MIN_NUMBER, MAX_NUMBER)
    found = False
    
    while not found:
        
        entry = input(f"\nEnter a number between {MIN_NUMBER} and {MAX_NUMBER} (or type 'cheat' to reveal the number): ")
        
        # Cheats
        if entry == "cheat":
            print(f"The number is {r}. But try guessing it without cheating next time!")
            continue
        elif entry == "specialcheat":
            print("\nGood job (with a little help), you guessed the number!")
            return
        
        while not entry.isdigit() or not (MIN_NUMBER <= int(entry) <= MAX_NUMBER):
            if not entry.isdigit():
                print("Please input a number.")
            else:
                print("Number out of range! Think about your behaviour.")
                time.sleep(10) # wait for 10 seconds
            entry = input(f"\nEnter a number between {MIN_NUMBER} and {MAX_NUMBER}: ")

        entry = int(entry)
        # Hints and conditions on what to do
        if abs(entry - r) > 250:
            print("You're way off!")
        elif entry == r:
            print(f"\n\nGood job, it was {r}!!!")
            found = True
        elif entry > r:
            print("You're too high!")
        else:
            print("A bit more?")

# Always start the game
while True:
    game()
    again = input("Do you want to play again? (yes/no): ")
    if again not in ["yes", "y"]:
        break

