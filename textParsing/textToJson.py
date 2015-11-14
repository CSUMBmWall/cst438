import json

with open('CleanedUp.txt', 'rt') as text:
    toConvert = []
    for x in text:
        toConvert.extend(x.lower().split(' '))
    toJson = {}
    for word in toConvert:
        if word in toJson:
            toJson[word] += 1
        else:
            toJson[word] = 1

sum = 0
for key in toJson:
    sum += toJson[key]
    
print(sum)
            
with open('finalJson.txt', 'wt') as theEnd:
    theEnd.writelines(json.dumps(toJson, sort_keys=True,indent=4, separators=(',', ': ')))
    