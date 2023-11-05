import random
import datetime
from time import sleep
import os

import asyncio
import keyboard

from rich.align import Align
from rich.text import Text

import menuk
from dialogue_parser import read


async def waitforkey(key: list | str) -> str | None:
    """
    list -> str: melyik key lett eloszor lenyomva\n
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

    await menuk.load()
    
    while True:
        x = await menuk.allomas_menu()
        match x:

            case "bolt":
                await menuk.bolt_menu()

            case "x":
                pass
        
        



asyncio.run(main())
