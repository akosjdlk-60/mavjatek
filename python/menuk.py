from rich.table import Table
from rich.style import Style
from rich.live import Live
from rich.layout import Layout
from rich.align import Align
from rich.text import Text
import datetime
from asyncio import sleep
from os import system as cmd
import os
import keyboard
import asyncio
from random import randint, choices
from dialogue_parser import read
import random

def update_opciok(opciok: list):
    global layout
    opcio_layout = Layout(name="tgzuiop")
    opcio_layout.split_column("")
    for opcio in opciok:
        opcio_layout.add_split(opcio)
    layout["opciok"].update(opcio_layout)

layout = Layout()

statok = {
    "penz": 0,
    "kaja": random.randint(50,100),
    "energia": random.randint(75,90),
    "varos": "Budapest",
    "rozsa": False,
    "jegy": False,
    "keregetett": False
}

inventory = {
    "Fánk": 0,
    "Sportszelet": 1,
    "Energiaital": 0
}

kovetkezo_vonat = [16, 32]
ido = datetime.datetime(year=2023, month=1, day=1, hour=8, minute=0)

async def load():
    global layout
    layout = ResetLayout()

    asyncio.create_task(clock())
    await asyncio.sleep(0.01)
    helper()
    live.start()
    penz = random.randint(0,250)
    await update_stats(statok, inventory)
    # await print_szoveg(read("allomasok budapest"), nev = "Akos", penz=penz)
    statok["penz"] += penz
    await update_stats(statok, inventory)


async def update_stats(statok: dict = statok, inventory: dict = inventory) -> None:
    global stattable
    global ido
    
    stattable = Table(show_edge=True, show_lines=False, show_header=False, expand=True)
    if statok["jegy"] == True:
        jegy = "Van"
    else: jegy = "Nincs"
    
    stattable.add_column(justify="center")
    stattable.add_column(justify="center")
    stattable.add_column(justify="center")

    stattable.add_row(f"Pénz: {statok['penz']}", f"{statok['varos']}", f"Idő: {time().strftime('%H:%M')}")
    stattable.add_row(f"Kaja: {statok['kaja']}%", f"Energia: {statok['energia']}%", f"Jegy: {jegy}")
    stattable.add_section()
    stattable.add_row(f"Fánk: {inventory['Fánk']}", f"Sportszelet: {inventory['Sportszelet']}", f"Energiaital: {inventory['Energiaital']}")


    layout["statok"].update(Align(stattable, "center", vertical="middle", pad=True))



def get_stats() -> dict:
    return statok

def get_inventory() -> dict:
    return inventory

def ResetLayout() -> Layout:
    global layout
    cmd('cls')

    # 2 fő rész
    layout.split_row(
        Layout(name="game"),
        Layout(name="nothing")
    ) 
    layout['game'].ratio = 1
    layout['nothing'].ratio = 1

    
    layout['game'].split_column(
        Layout(name="jatekter"),
        Layout(name="toolbar")
    )
    
    layout['jatekter'].split_row(
        Layout(name="opciok"),
        Layout(name="szoveg")
    )
    
    layout['toolbar'].split_row(
        Layout(name="help"),
        Layout(name="statok")
    )

    # Méretek
    layout['jatekter'].size=None
    layout['statok'].size=None
    layout['opciok'].size=None
    layout['szoveg'].size=None
    
    layout['jatekter'].ratio=4
    layout['toolbar'].ratio=1
    layout['opciok'].ratio=1
    layout['szoveg'].ratio=2
    layout['statok'].ratio=2
    
    layout['nothing'].update("")
    layout['game'].update("")
    layout['szoveg'].update("")
    layout['statok'].update("")
    layout["opciok"].update("")
    layout["help"].update("")
    
    return layout


def helper():
    helptable = Table(show_edge=False, show_lines=False, show_header=False, expand=False)
    helptable.add_column(justify = "left")
    helptable.add_row("1-9: Opciók")
    helptable.add_row("Space: Tovább")
    helptable.add_row("r: Frissítés")
    layout['help'].update(Align(helptable, "center", vertical="middle", pad=True))


def update_opciok(opciok: list):
    global layout
    table = Table(show_edge=False, show_lines=False, show_header=False, expand=True, padding=(1, 0))
    i=1
    for opcio in opciok:
        table.add_row(Text(f"{i} - {opcio}"))
        i+=1
    
    layout['opciok'].update(table)


async def allomas_menu() -> str:
    global statok
    global inventory
    global kovetkezo_vonat
    
    jegy_ar = randint(500, 600)
    update_opciok(["Séta a boltba (1 óra)", "Futás a boltba (0.5 óra)", f"Jegyvásárlás ({jegy_ar} Pénz)", f"Vár, majd felszáll a vonatra {kovetkezo_vonat[0]}:{kovetkezo_vonat[1]}-kor", "Kisgyerek meglopása (+100 - +250 Pénz)", "Öltönyös úriember meglopása (+300 - +600 Pénz)", "Kéregetés"])
    x = await waitforkey(["1", "2", "3", "4", "5", "6", "7", "8"])
    match x:
        
        case 1:
            await print_szoveg(read("menu allomas seta"))
            add_time(60)
            return "bolt"
        
        case 2:
            await print_szoveg(read("menu allomas futas"))
            add_time(30)
            return "bolt"
        
        case 3:
            eleg = statok["penz"] >= jegy_ar
            if eleg:
                await print_szoveg(read("menu allomas jegyVasarlas"), )
                statok["penz"] -= jegy_ar
                statok["jegy"] = True
                return "allomas"
            
            else:
                await print_szoveg(read("menu allomas jegyVasarlasNincsPenz"))
                return "allomas"
        
        case 4:
            await print_szoveg(read("menu allomas felszallas"))
            set_time(kovetkezo_vonat[0], kovetkezo_vonat[1])
            return "vonat"
        
        case 5:
            lop_osszeg = randint(100, 250)
            await print_szoveg(read("menu allomas lopasGyerek"), False, penz=lop_osszeg)
            if choices(["lecsuktak", lop_osszeg], weights=[10, 100])[0] == "lecsuktak":
                await print_szoveg(read("menu allomas elkapnak"))
                await print_szoveg(["Lecsuktak, Game Over", " "])
                keyboard.send(hotkey='alt+F4')
                
            
        case 6:
            lop_osszeg = randint(100, 250)
            await print_szoveg(read("menu allomas lopasFerfi"), False, penz=lop_osszeg)
            if choices(["lecsuktak", lop_osszeg], weights=[40, 100])[0] == "lecsuktak":
                await print_szoveg(read("menu allomas elkapnak"), False)
                await print_szoveg(["Lecsuktak, Game Over"], False)
                keyboard.send(hotkey='alt+f4')

        case 7:
            keregetes_osszeg = randint(100, 250)
            

        case 8:
            pass


async def vonat_menu() -> str:
    global statok
    global inventory
    update_opciok(["Leszáll", "Alszik a következő állomásig", "Bliccelés a WC-ben"])
    x = waitforkey(3)
    match x:
        case 1:
            pass
        
        case 2:
            pass
        
        case 3:
            pass


async def bolt_menu() -> list:
    global statok
    global inventory
    update_opciok(["Energiaital vásárlás", "Sportszelet vásárlás", "Fánk vásárlás", "Virág vásárlás", "Virág lopás", "Étel lopás", "Séta az állomásra", "Futás az állomásra"])
    x = await waitforkey(8)
    match x:
        case 1:
            pass
        
        case 2:
            pass

        case 3:
            pass

        case 4:
            pass

        case 5:
            pass

        case 6:
            pass

        case 7:
            pass

        case 8:
            pass


async def waitforkey(key: list | str | int) -> int | None:
    """
    list -> int melyik key lett eloszor lenyomva\n
    int -> int-ből listát csinál: ex: 6 -> 1,2,3,4,5,6 \n 
    str -> None: var amig le nem lett nyomva majd tovabblep (semmit nem csinal)
    """
    while True:
        event = keyboard.read_event(suppress=True)
        if event.name == "esc":
            break
        
        if type(key) == list:
            for i in range(len(key)):
                if event.name == key[i]:
                    return i+1
        elif type(key) == str and event.name == key:
            return None



async def clock():
    global ido
    while True:
        await sleep(1)
        ido += datetime.timedelta(minutes=1)
        await update_stats()

def time():
    return ido

def set_time(hour:int, minute:int):
    global ido
    ido = datetime.datetime(year=ido.year, month=ido.month, day=ido.day, hour=hour, minute=minute)


def add_time(change: int):
    """
    change: Hány perc időt adjunk hozzá.
    """
    global ido
    ido += datetime.timedelta(minutes=change)


async def print_szoveg(szovegz: list, tovabb: bool, **kwargs):
    global layout
    for i in range(len(szovegz)):
        string = ""
        for j in range(len(szovegz[i])):
            try:
                string += szovegz[i].format(**kwargs)[j]
            except IndexError:
                pass
            layout['szoveg'].update(Align(string, "center", vertical="middle"))
            await asyncio.sleep(0.01)

        if tovabb:
            if i != len(szovegz)-1:
                await waitforkey("space")
        else: await waitforkey("space")






live = Live(layout, auto_refresh=True, refresh_per_second=120)

