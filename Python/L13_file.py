# L13: https://reurl.cc/mvEon9

file = open("L13_data.txt", mode = "w", encoding = "utf-8")
file.write("5\n3\n10")
file.close()

with open("L13_data_notNeedClose.txt", mode= "w") as file:
    file.write("Hi~~~~~~")

with open("L13_data.txt", mode= "r", encoding = "utf-8") as file:
    data = file.read()
print(data)

sum = 0
with open("L13_data.txt", mode= "r", encoding = "utf-8") as file:
    for line in file:
        sum += int(line)
print(sum)

print("################")

import json
with open("L13_config.json", mode = "r") as file:
    data = json.load(file)

print(data)
print("name: ", data["name"])
print("version: ", data["version"])

data["name"] = "New Name"
print(data)

with open("L13_config.json", mode = "w") as file:
    data = json.dump(data ,file)
