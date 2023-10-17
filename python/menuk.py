from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich.screen import Screen
from rich.live import Live
from rich.layout import Layout
import time
from os import system as cmd
from os import get_terminal_size

console = Console(force_terminal=True)
stattable = Table(show_edge=True, show_lines=False, show_header=False)

def statmenu(statok: dict, inventory: dict) -> None:
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
def screen():
    cmd('cls')
    layout.split_row(
        Layout(name="game"),
        Layout(name="nothing")
    )
    layout['game'].ratio = 1
    layout['nothing'].ratio = 1
    layout['game'].split_column(
        Layout(name="jatekter"),
        Layout(name="statok")
    )
    
    layout['jatekter'].split_row(
        Layout(name="opciok"),
        Layout(name="szoveg"),
    )
    layout['jatekter'].size=None
    layout['statok'].size=None
    layout['opciok'].size=None
    layout['szoveg'].size=None

    layout['jatekter'].ratio=4
    layout['statok'].ratio=1
    layout['opciok'].ratio=1
    layout['szoveg'].ratio=2

    # console.print(layout)
 
    with Live(layout, auto_refresh=False) as live:
        x = get_terminal_size().lines
        while True:
            y = get_terminal_size().lines

            if x != y:
                live.refresh()
                x = y




screen()
