import random
import datetime
from time import sleep
import os

import asyncio
import keyboard

from rich.align import Align
from rich.text import Text

import menuk
import dialogue_parser as parser

keyboard.press('f11')

async def waitforkey(key: list | str | int) -> str | None:
    """
    list -> str: melyik key lett eloszor lenyomva\n
    int -> str: int-ből listát csinál: ex: 6 -> 1,2,3,4,5,6 ->\n 
    str -> None: var amig le nem lett nyomva majd tovabblep (semmit nem csinal)
    """
    while True:
        event = keyboard.read_event(suppress=True)
        if event.name == "esc":
            break
        
        if type(key) == list:
            for i in range(len(key)):
                if event.name == key[i]:
                    return event.name
        elif type(key) == str and event.name == key:
            return None

async def hotkeys():
    def pressed_key(e: keyboard.KeyboardEvent):
        match e.name:

            case "r":
                return

            case "esc":
                menuk.live.stop()
                exit(0)

                

    keyboard.on_release(pressed_key, suppress=True)

async def main():
    asyncio.create_task(hotkeys())
    await asyncio.sleep(0.01)
    asyncio.create_task(menuk.clock())
    await asyncio.sleep(0.01)

    global statok
    global inventory
    
    statok = {
        "penz": random.randint(0,250),
        "kaja": random.randint(50,100),
        "energia": random.randint(75,90),
        "varos": "Budapest",
        "rozsa": False,
        "jegy": False
    }
    
    inventory = {
        "Fánk": 0,
        "Sportszelet": 1,
        "Energiaital": 0
    }

    global layout
    layout = menuk.ResetLayout()
    menuk.helper()
    menuk.update_stats(statok, inventory)
    menuk.live.start()
    while True:
        
        
        szovegz = []; i:str
        for i in parser.read('eventek varos penz'):
            x=random.choices(population=(20, 50, 100, 200, 500), weights=(5,4,3,2,1))
            szovegz.append(i.format(x=x[0]))
        statok["penz"] += x[0]
        menuk.update_stats(statok, inventory)
        await print_szoveg(szovegz)
                

async def print_szoveg(renderable: list):
    global layout
    for i in range(len(renderable)):
        string = ""
        for j in range(len(renderable[i])):
            string += renderable[i][j]
            layout['szoveg'].update(Align(string, "center", vertical="middle"))
            await asyncio.sleep(0.01)
        await waitforkey("space")



asyncio.run(main())