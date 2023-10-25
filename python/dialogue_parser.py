import json

with open("dialogues.json", "r", encoding="utf-8") as f:
    dialogues = json.load(f)


def read(input: list): #input = ["meghalt"]["ehseg"]
    output = dialogues
    for key in input:
        output= output[key]
    return output

# x= 3456
# print(str(read(['meghalt', 'ehseg'])).format(x=x))