import re

def findSentences(text):
    sentence_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
    sentences = re.split(sentence_pattern, text)
    for sentence in sentences:
        print(f"{sentence} \n")

text = "- Dr. Johnson: Hello guys, I'm Dr. Johnson and I'm 36 years old.Do you know about the web scrsping and web crawling?- Mr. Brown: Hi Dr. Johnson, sorry I don't know but I think it's a amazing thing."
findSentences(text)