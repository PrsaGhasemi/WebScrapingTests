import random 

selectedNumber = random.randint(1,20)
userChances = 5
userLost = True
while userChances:
    try:
        userGuess = int(input("Enter your guess here: "))
        if userGuess == selectedNumber:
            userLost = False
            break
        elif not userGuess in range(1,20):
            print("You can only enter numbers between 1,20: ")
        else :
            userChances = userChances - 1
            print(f"Your guess was wrong, you have {userChances} chances left!")

    except ValueError:
        print("Your can only enter numbers between 1-20: ")


if userLost:
    print(f"You lost! the answer was {selectedNumber}")
else:
    print("You Won!")   
    