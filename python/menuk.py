from rich.console import Console
from rich.table import Table
from rich.style import Style

def statmenu(statok: dict, inventory: dict) -> None:
    if statok["jegy"] == True:
        jegy = "Van"
    else: jegy = "Nincs"
    
    # print("\n_______________________________________________________________")
    # print(f'\nPénz: {statok["penz"]} Ft\t\t{statok["varos"]}-{statok["idojaras"]}\t\tIdő: {statok["ido"]}')
    # print(f'\nKaja: {statok["kaja"]}%\t\tEnergia: {statok["energia"]}%\t\tJegy: {jegy}')
    # print(f'\n\t\t\t  Inventory\n\t\t       ---------------\nFánk: {inventory["Fánk"]}\t\t\tSportszelet: {inventory["Sportszelet"]}\t\tEnergiaital: {inventory["Energiaital"]}')
    # print(  "_______________________________________________________________")


    table = Table(show_edge=True, show_lines=False, show_header=False)
    table.add_column(justify="center")
    table.add_column(justify="center")
    table.add_column(justify="center")

    table.add_row(f"Pénz: {statok['penz']}", f"{statok['varos']} - {statok['idojaras']}", f"Idő: {statok['ido']}")
    table.add_row(f"May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    table.add_row(f"Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")

    console = Console()
    console.print(table, justify="center")

"""

row("", "", "")
row("", "", "")
row("", "", "")

"""
