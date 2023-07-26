finalList = []
i = 0
while i <= 20 :
    enteredText = input("Enter your text here, you can send both English & Persian texts: ")
    if len(enteredText) <= 100:
        print("your text should at least contain 100 words")
    else :
        finalList.append(enteredText)
        i = i + 1
    if i > 20:
        break

def classify_text(texts):
    i = 0
    emotional_keywords = ["joy", "excitement", "happy", "love", "appreciate", "محبت", "خوشحالی", "شادی", "مهربانی"]
    logical_keywords = ["logical", "reason", "evidence", "analyze", "منطقی", "تحلیل" , "بررسی" , "آمار" , "علم"]
    advertisement_keywords = ["buy", "sale", "discount", "limited time offer", "خرید", "فروش", "تخفیف", "پیشنهاد محدود"]
    for text in texts:
        i = i + 1
        text_lower = text.lower()
        word_count = len(text_lower.split(" "))
        emotional_count = sum(text_lower.count(keyword) for keyword in emotional_keywords)
        logical_count = sum(text_lower.count(keyword) for keyword in logical_keywords)
        advertisement_count = sum(text_lower.count(keyword) for keyword in advertisement_keywords)
        emotional_percentage = (emotional_count / word_count) * 100
        logical_percentage = (logical_count / word_count) * 100
        advertisement_percentage = (advertisement_count / word_count) * 100
        print(f"The text number {i} is {emotional_percentage}% emotional \n {logical_percentage}% logical \n {advertisement_percentage}% advertisements")


classify_text(finalList)