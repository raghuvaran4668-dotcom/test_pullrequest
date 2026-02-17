import random
while True:
    user_input = input("Roll the dice? (yes/no): ").lower()
    if user_input == "yes":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"{die1}, {die2}")
    elif user_input == "no":
        print("Thanks for playing, maybe next time!")
        break
    else:
        print("Invalid choice, please enter 'yes' or 'no'.")
        
     


