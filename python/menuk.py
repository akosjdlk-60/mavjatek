from rich.table import Table
from rich.style import Style
from rich.screen import Screen
from rich.live import Live
from rich.layout import Layout
from rich.align import Align
from rich.text import Text
import datetime
from asyncio import sleep
from os import system as cmd
import os
import keyboard


def update_opciok(opciok: list):
    global layout
    print("asd")
    opcio_layout = Layout(name="tgzuiop")
    opcio_layout.split_column("")
    for opcio in opciok:
        opcio_layout.add_split(opcio)
    layout["opciok"].update(opcio_layout)


def update_stats(statok: dict, inventory: dict) -> None:
    global stattable
    stattable = Table(show_edge=True, show_lines=False, show_header=False, expand=True)
    if statok["jegy"] == True:
        jegy = "Van"
    else: jegy = "Nincs"
    
    stattable.add_column(justify="center")
    stattable.add_column(justify="center")
    stattable.add_column(justify="center")

    stattable.add_row(f"Pénz: {statok['penz']}", f"{statok['varos']}", f"Idő: {time()}")
    stattable.add_row(f"Kaja: {statok['kaja']}%", f"Energia: {statok['energia']}%", f"Jegy: {jegy}")
    stattable.add_section()
    stattable.add_row(f"Fánk: {inventory['Fánk']}", f"Sportszelet: {inventory['Sportszelet']}", f"Energiaital: {inventory['Energiaital']}")


    layout["statok"].update(Align(stattable, "center", vertical="middle", pad=True))




layout = Layout()
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


async def allomas_menu(statok: dict, kovetkezo_vonat: list) -> list:
    """
    list[0] -> str: kovetkezo menu amit hivni kell
    list[1] -> dict: statok dict, UPDATELD!!!
    """
    update_opciok(["Séta a boltba (1 óra)", "Futás a boltba (0.5 óra)", f"Vár, majd felszáll a vonatra {kovetkezo_vonat[0]}:{kovetkezo_vonat[1]}-kor", "Kisgyerek meglopása (+100-250 Pénz)", "Öltönyös úriember meglopása (+300-600 Pénz)"])
    x = await waitforkey(5)
    match x:
        
        case 1:
            add_time(60)
            return "bolt", statok
        
        case 2:
            add_time(30)
            return "bolt", statok
        
        case 3:
            set_time(kovetkezo_vonat)
            return "vonat", statok
        
        case 4:
            pass
        
        case 5:
            pass


async def vonat_menu(statok: dict) -> list:
    """
    list[0] -> str: kovetkezo menu amit hivni kell
    list[1] -> dict: statok dict, UPDATELD!!!
    """
    update_opciok(["Leszáll", "Alszik a következő állomásig", "Bliccelés a WC-ben"])
    x = await waitforkey(3)
    match x:
        case 1:
            pass
        
        case 2:
            pass
        
        case 3:
            pass


async def bolt_menu(statok: dict) -> list:
    """
    list[0] -> str: kovetkezo menu amit hivni kell
    list[1] -> dict: statok dict, UPDATELD!!!
    """
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
                    return i
        elif type(key) == str and event.name == key:
            return None





async def clock():
    global ido
    ido = datetime.datetime(year=2023, month=1, day=1, hour=8, minute=0)
    while True:
        await sleep(1)
        ido += datetime.timedelta(minutes=1)

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





live = Live(layout, auto_refresh=True, refresh_per_second=120)
