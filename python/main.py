import random
import datetime
from time import sleep
import os
import json
import asyncio

from rich.console import Console
from rich.live import Live

import menuk
from keyboardManager import *

console = Console()

with open("dialogues.json", "r", encoding="utf-8") as f:
    x = f.read()
    dialogues = json.loads(x)
    # print(str(dialogues["story"]["Bécs"]["dancika"]).format(nev="Akos"))
    
    
async def main():
    asyncio.create_task(waitforkey())
    await asyncio.sleep(0)
    print("asd")
    os.system("cls")
    global statok
    global inventory
    

    statok = {
        "penz": random.randint(0,250),
        "kaja": random.randint(50,100),
        "energia": random.randint(75,90),
        "ido": datetime.time(8,0).strftime("%H:%M"),
        "varos": "Budapest",
        "idojaras": "Napos",
        "rozsa": False,
        "jegy": False
    }
    
    inventory = {
        "Fánk": 0,
        "Sportszelet": 1,
        "Energiaital": 0
    }

    layout = menuk.mainLayout()
    global live
    with Live(layout, auto_refresh=False) as live:
        while True:
            menuk.update_opciok(["ELSO", "mASOdik", "harmadik", "asd"])
            refresh_screen()



        
            


def refresh_screen():
    live.refresh()


asyncio.run(main())