enteredString = input("put your text here: ")
stringCharacterAmount = 0
for _ in enteredString:
    if not _ == " ":
        stringCharacterAmount = stringCharacterAmount + 1
    
print(f"there are {stringCharacterAmount} characters in your text.")