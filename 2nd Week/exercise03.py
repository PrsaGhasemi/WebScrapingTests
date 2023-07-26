import re

def extractUrls(text):

    urlPattern = r'https?://(?:www\.)?[\w-]+(?:\.[\w-]+)+[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-]'
    
    # Find all matches of the URL pattern in the text
    urls = re.findall(urlPattern, text)
    if urls:
        for url in urls:
            print(f"{url} \n")
    else:
        print("There is no url in your text!")
    
userText = input("Enter your text here: ")
extractUrls(userText)
