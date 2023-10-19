from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich.screen import Screen
from rich.live import Live
from rich.layout import Layout
import time
from os import system as cmd


console = Console(force_terminal=True)
stattable = Table(show_edge=True, show_lines=False, show_header=False)


def update_opciok(opciok: list):
    global layout
    print("asd")
    opcio_layout = Layout(name="tgzuiop")
    opcio_layout.split_column("")
    for opcio in opciok:
        opcio_layout.add_split(opcio)
    layout["opciok"].update(opcio_layout)


def update_stats(statok: dict, inventory: dict) -> None:
    if statok["jegy"] == True:
        jegy = "Van"
    else: jegy = "Nincs"
    
    stattable.add_column(justify="center")
    stattable.add_column(justify="center")
    stattable.add_column(justify="center")

    stattable.add_row(f"Pénz: {statok['penz']}", f"{statok['varos']} - {statok['idojaras']}", f"Idő: {statok['ido']}")
    stattable.add_row(f"Kaja: {statok['kaja']}%", f"Energia: {statok['energia']}%", f"Jegy: {jegy}")
    stattable.add_section()
    stattable.add_row(f"Fánk: {inventory['Fánk']}", f"Sportszelet: {inventory['Sportszelet']}", f"Energiaital: {inventory['Energiaital']}")


layout = Layout()
def mainLayout() -> Layout:
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

    # screen fele ures
    # layout['nothing'].update("")
    # layout['game'].update("")
    # layout['help'].update("")
    # layout['szoveg'].update("")
    # layout['statok'].update("")

    return layout
    

        
        

def update_layout(layout_name: str, renderable):
    global layout
    layout[layout_name].update(renderable)

def update_opciok(opciok: list):
    global layout
    opciok_layout = Layout()

    i=1
    for opcio in opciok:
        opciok_layout.add_split(f"{i}-{opcio}")
        i+=1
    
        

    layout['opciok'].update(opciok_layout)
