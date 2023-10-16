import random
import datetime
from time import sleep
import menuk
import os
from rich.console import Console

console = Console()

def main():

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

        # Game
        while True:
            os.system("cls")
            console.print("MÁV Játék", style="bold blue")
            menuk.statmenu(statok, inventory)
            sleep(1)

main()