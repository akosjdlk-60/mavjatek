import json

with open("dialogues.json", "r", encoding="utf-8") as f:
    dialogues = json.load(f)


def read(input: str): #input = "meghalt ehseg"
    output = dialogues
    x= input.split(" ")
    for key in x:
        output = output[key]
    return output
