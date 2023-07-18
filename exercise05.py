enteredText = input("enter your text here: ")
unwantedSymbols = [",", ".", "?", "!"]
words = enteredText.split(" ")

hashtags = list(filter(lambda word: word.startswith("#"), words))
mentions = list(filter(lambda word: word.startswith("@"), words))
symbolRemover = lambda entryText: ''.join([word for word in entryText if word not in unwantedSymbols])
editedText = symbolRemover(list(enteredText))

print(f"Hashtags: {hashtags}")
print(f"Mentions: {mentions}")
print(f"EditedText: {editedText}")