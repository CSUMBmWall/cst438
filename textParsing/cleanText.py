import string

jsonDic = {}
megaLine = ''

with open('theText.txt', 'rt') as toConvert:
    for line in toConvert:
        megaLine += ' ' + line
        
exclude = set(string.punctuation)
#megaLine = ''.join(character for character in megaLine if character not in exclude)
for x in exclude:
    megaLine = megaLine.replace(x, ' ')

#for i in range(0, len(megaLine) - 1):
#    print(megaLine[i])
with open('test.txt', 'wt') as test:
    test.writelines(megaLine)