from bs4 import BeautifulSoup
#import html2text

with open("convert.html", 'rb') as toConvert:
    soup = BeautifulSoup(toConvert, 'html.parser')
    converted = soup.get_text()
    #print(converted)
with open("theText.txt", 'wb') as toWrite:
    toWrite.write(bytes(converted, 'utf8'))