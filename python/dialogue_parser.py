import json
import os

path = f"{os.path.abspath(os.getcwd())}\\"
with open(f"{path}python\\dialogues.json", "r", encoding="utf-8") as f:
    dialogues = json.load(f)


def read(input: str) -> list:  # input = "meghalt ehseg"
    output = dialogues
    x = input.split(" ")
    for key in x:
        output = output[key]
    return output
