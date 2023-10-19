import random
import datetime
from time import sleep
import os
import json
import asyncio

from rich.console import Console
from rich.live import Live
from rich.align import Align

import menuk
import keyboard

console = Console()

with open("dialogues.json", "r", encoding="utf-8") as f:
    x = f.read()
    dialogues = json.loads(x)
    # print(str(dialogues["story"]["Bécs"]["dancika"]).format(nev="Akos"))
    

async def waitforkey(key: list | str | int) -> str | None:
    """
    list -> str: melyik key lett eloszor lenyomva\n
    int -> str: int-ből listát csinál: ex: 6 -> 1,2,3,4,5,6 ->\n 
    str -> None: var amig le nem lett nyomva majd tovabblep (semmit nem csinal)
    """
    while True:
        event = keyboard.read_event(suppress=True)
        if type(key) == list:
            for i in range(len(key)):
                if event.name == key[i]:
                    return event.name
        elif type(key) == str and event.name == key:
            return None

async def hotkeys():
    def print_pressed_keys(e: keyboard.KeyboardEvent):
        print(e.name)

        match e.name:

            case "f5":
                refresh_screen()

            case "esc":
                asyncio.Task.cancel(hotkeys())
                

    keyboard.on_release(print_pressed_keys, suppress=True)

async def main():
    asyncio.create_task(hotkeys())
    await asyncio.sleep(0)

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
            
            menuk.update_opciok(["ELSO", "mASOdik", "harmadik", "asd"], )
            refresh_screen()
            await waitforkey("space")
            menuk.update_layout("szoveg", Align.center("a kurva anyad", vertical="middle"))
            # await asyncio.sleep(100)

        



def refresh_screen():
    live.refresh()


asyncio.run(main())