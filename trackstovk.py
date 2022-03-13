import json

with open("errors.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

n = 0
for num, strtrack in jsonObject.items():
    print(num,strtrack)
    n+=1
print(n)