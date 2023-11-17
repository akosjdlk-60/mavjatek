from rich.table import Table
from rich.padding import Padding
from rich.live import Live
from rich.layout import Layout
from rich.align import Align
from rich.text import Text
import datetime
from asyncio import sleep
from os import system as cmd
from pynput import keyboard
from pynput.keyboard import Key
import asyncio
from random import randint, choices
from dialogue_parser import read
import random

layout = Layout()

statok = {
    "penz": 0,
    "kaja": random.randint(50, 100),
    "energia": random.randint(75, 100),
    "varos": "Budapest",
    "rozsa": False,
    "jegy": False,
    "keregetett": False,
}

jegy_ar = 500
energiaital_ar = 500
sportszelet_ar = 200
fank_ar = 180
rozsa_ar = 1000

inventory = {"Fánk": 0, "Sportszelet": 1, "Energiaital": 0}

kovetkezo_vonat = [16, 32]
ido = datetime.datetime(year=2023, month=1, day=1, hour=8, minute=0)


async def load():
    global layout
    layout = ResetLayout()

    asyncio.create_task(tick())
    await asyncio.sleep(0.01)
    helptable = Table(
        show_edge=False, show_lines=False, show_header=False, expand=False
    )
    helptable.add_column(justify="left")
    helptable.add_column(justify="left")
    helptable.add_row("1-9: Opciók", "Q: Fánk evés")
    helptable.add_row("Space: Tovább", "W: Sportszelet evés")
    helptable.add_row("", "E: Energiaital ivás")
    layout["help"].update(Align(helptable, "center", vertical="middle", pad=True))
    live.start()
    penz = choices([50, 100, 200])[0]
    keyboard.Controller().press(Key.f11)
    await print_szoveg([" START\n\n[Space]"], False)
    await print_szoveg(read("allomasok budapest"), True, penz=penz)
    statok["penz"] += penz
    update_stats(statok, inventory)


def update_stats(statok: dict = statok, inventory: dict = inventory) -> None:
    global stattable
    global ido

    stattable = Table(show_edge=True, show_lines=False, show_header=False, expand=True)
    if statok["jegy"]:
        jegy = "Van"
    else:
        jegy = "Nincs"
    if statok["rozsa"]:
        rozsa = "Van"
    else:
        rozsa = "Nincs"

    stattable.add_column(justify="center")
    stattable.add_column(justify="center")
    stattable.add_column(justify="center")

    stattable.add_row(
        f"Pénz: {statok['penz']} Ft",
        f"{statok['varos']}",
        f"Idő: {ido.strftime('%H:%M')}",
    )
    stattable.add_row(
        f"Kaja: {int(statok['kaja'])}%",
        f"Energia: {int(statok['energia'])}%",
        f"Jegy: {jegy}",
    )
    stattable.add_row("", f"Virág: {rozsa}", "")
    stattable.add_section()
    stattable.add_row(
        f"Fánk: {inventory['Fánk']}",
        f"Sportszelet: {inventory['Sportszelet']}",
        f"Energiaital: {inventory['Energiaital']}",
    )

    layout["statok"].update(Align(stattable, "center", vertical="middle", pad=True))


def get_stats() -> dict:
    return statok


def get_inventory() -> dict:
    return inventory


def ResetLayout() -> Layout:
    global layout
    cmd("cls")

    # 2 fő rész
    layout.split_row(Layout(name="game"), Layout(name="nothing"))
    layout["game"].ratio = 2
    layout["nothing"].ratio = 1

    layout["game"].split_column(Layout(name="jatekter"), Layout(name="toolbar"))

    layout["jatekter"].split_row(Layout(name="opciok"), Layout(name="szoveg"))

    layout["toolbar"].split_row(Layout(name="help"), Layout(name="statok"))

    # Méretek
    layout["jatekter"].size = None
    layout["statok"].size = None
    layout["opciok"].size = None
    layout["szoveg"].size = None

    layout["jatekter"].ratio = 4
    layout["toolbar"].ratio = 1
    layout["opciok"].ratio = 1
    layout["szoveg"].ratio = 2
    layout["statok"].ratio = 2

    layout["nothing"].update("")
    layout["game"].update("")
    layout["szoveg"].update("")
    layout["statok"].update("")
    layout["opciok"].update("")
    layout["help"].update("")

    return layout


def update_opciok(opciok: list):
    global layout
    table = Table(
        show_edge=False, show_lines=False, show_header=False, expand=True, padding=1
    )
    i = 1
    for opcio in opciok:
        table.add_row(Text(f"{i} - {opcio}"))
        i += 1

    layout["opciok"].update(table)


async def allomas_menu() -> str:
    global statok
    global inventory
    global kovetkezo_vonat
    global jegy_ar

    if statok["keregetett"]:
        update_opciok(
            [
                "Séta a boltba (1 óra)",
                "Futás a boltba (fél óra)",
                f"Jegyvásárlás ({jegy_ar} Ft)",
                f"Vársz, majd felszállsz a vonatra {kovetkezo_vonat[0]}:{kovetkezo_vonat[1]}-kor",
                "Kisgyerek meglopása (100 - 250 Ft)",
                "Öltönyös úriember meglopása (300 - 600 Ft)",
            ]
        )
        x = await waitforkey(["1", "2", "3", "4", "5", "6"])
    else:
        update_opciok(
            [
                "Séta a boltba (1 óra)",
                "Futás a boltba (fél óra)",
                f"Jegyvásárlás ({jegy_ar} Ft)",
                f"Vársz, majd felszállsz a vonatra {kovetkezo_vonat[0]}:{kovetkezo_vonat[1]}-kor",
                "Kisgyerek meglopása (100 - 250 Ft)",
                "Öltönyös úriember meglopása (300 - 600 Ft)",
                "Kéregetés",
            ]
        )
        x = await waitforkey(["1", "2", "3", "4", "5", "6", "7"])

    match x:
        case 1:
            statok["energia"] -= 15
            add_time(60)
            sleep(0.01)
            if statok["energia"] <= 0:
                statok["energia"] = 0
                update_stats()
                await print_szoveg(read("meghalt energia"), False)
                exit(0)
            event = choices(
                ["rablas", 500, 200, 50, 10, "semmi"], weights=[7, 8, 12, 18, 20, 35]
            )
            match event[0]:
                case "semmi":
                    await print_szoveg(read("menu allomas seta"), True)

                case 500:
                    await print_szoveg(["Elkezdesz sétálni a bolt felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=500)
                    statok["penz"] += 500
                    update_stats()

                case 200:
                    await print_szoveg(["Elkezdesz sétálni a bolt felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=200)
                    statok["penz"] += 200
                    update_stats()

                case 50:
                    await print_szoveg(["Elkezdesz sétálni a bolt felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=50)
                    statok["penz"] += 50
                    update_stats()

                case 10:
                    await print_szoveg(["Elkezdesz sétálni a bolt felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=10)
                    statok["penz"] += 10
                    update_stats()

                case "rablas":
                    szazalek = randint(15, 50) / 100
                    penz = statok["penz"]
                    elveszt = penz - penz * szazalek
                    await print_szoveg(["Elkezdesz sétálni a bolt felé..."], False)
                    await print_szoveg(
                        read("eventek varos rablas"), True, penz=int(penz - elveszt)
                    )
                    statok["penz"] -= int(elveszt)
                    update_stats(statok)
                    add_time(15)

            return "bolt"

        case 2:
            statok["energia"] -= 30
            add_time(30)
            sleep(0.01)
            if statok["energia"] <= 0:
                statok["energia"] = 0
                update_stats()
                await print_szoveg(read("meghalt energia"), False)
                exit(0)
            event = choices(
                ["rablas", 500, 200, 50, 10, "semmi"], weights=[10, 5, 12, 18, 20, 35]
            )
            match event[0]:
                case "semmi":
                    await print_szoveg(read("menu allomas futas"), True)

                case 500:
                    statok["penz"] += 500
                    update_stats()
                    await print_szoveg(["Elkezdesz futni a bolt felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=500)

                case 200:
                    statok["penz"] += 200
                    update_stats()
                    await print_szoveg(["Elkezdesz futni a bolt felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=200)

                case 50:
                    statok["penz"] += 50
                    update_stats()
                    await print_szoveg(["Elkezdesz futni a bolt felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=50)

                case 10:
                    statok["penz"] += 10
                    update_stats()
                    await print_szoveg(["Elkezdesz futni a bolt felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=10)

                case "rablas":
                    szazalek = randint(15, 50) / 100
                    penz = statok["penz"]
                    elveszt = penz - penz * szazalek
                    statok["penz"] -= int(elveszt)
                    update_stats(statok)
                    await print_szoveg(["Elkezdesz sétálni a bolt felé..."], False)
                    await print_szoveg(
                        read("eventek varos rablas"), True, penz=int(penz - elveszt)
                    )
                    add_time(15)

            return "bolt"

        case 3:
            eleg = statok["penz"] >= jegy_ar
            if eleg:
                await print_szoveg(read("menu allomas jegyVasarlas"), True)
                statok["penz"] -= jegy_ar
                statok["jegy"] = True
                update_stats()
                return "allomas"

            else:
                await print_szoveg(read("menu allomas jegyVasarlasNincsPenz"), True)
                return "allomas"

        case 4:
            await print_szoveg(read("menu allomas felszallas"), False)
            set_time(kovetkezo_vonat[0], kovetkezo_vonat[1])
            return "vonat"

        case 5:
            lop_osszeg = randint(100, 250)
            await print_szoveg(read("menu allomas lopasGyerek"), False, penz=lop_osszeg)
            statok["penz"] += lop_osszeg
            update_stats()
            if choices(["lecsuktak", lop_osszeg], weights=[30, 70])[0] == "lecsuktak":
                await print_szoveg(read("menu allomas elkapnak"), False)
                exit(0)

        case 6:
            lop_osszeg = randint(300, 600)
            await print_szoveg(read("menu allomas lopasFerfi"), False, penz=lop_osszeg)
            statok["penz"] += lop_osszeg
            update_stats()
            if choices(["lecsuktak", lop_osszeg], weights=[50, 50])[0] == "lecsuktak":
                await print_szoveg(read("menu allomas elkapnak"), False)
                exit(0)

        case 7:
            keregetes_osszeg = randint(100, 250)
            await print_szoveg(
                read("menu allomas keregetes"), True, penz=keregetes_osszeg
            )
            statok["keregetett"] = True
            statok["penz"] += keregetes_osszeg
            update_stats()


async def vonat_menu() -> str:
    global statok
    global inventory
    update_opciok(["Ülsz a helyeden, várod az ellenőrt", "Bliccelés a WC-ben"])
    await print_szoveg(read("menu vonat indulas"), True)
    x = await waitforkey(["1", "2"])
    match x:
        case 1:
            if statok["jegy"]:
                await print_szoveg(read("menu vonat jegyVan"), False)
                statok["jegy"] = False
            else:
                ########## nincs jegy ##########
                penz = statok["penz"]
                await print_szoveg(read("menu vonat jegyNincs"), False, penz=1000)
                if penz < 1000:
                    await print_szoveg(read("menu vonat jegyNincsPenzNincs"), False)
                    exit(0)
                else:
                    await print_szoveg(["Kifizeted a bírságot..."], True)
                    statok["penz"] -= 1000

        case 2:
            await print_szoveg(
                [
                    "Mivel nem akarod, hogy megbüntessen, elbújsz a közeli WC-ben. Ez egy örökkévalóság lesz... (2 perc)"
                ],
                True,
            )
            await sleep(120)
            await print_szoveg(read("menu vonat blicceles"), True)

    update_opciok(["Alvás a következő állomásig", "Ülsz és gondolkozol"])
    x = await waitforkey(["1", "2"])
    match x:
        case 1:
            await print_szoveg(read("menu vonat alvas"), False)
            statok["energia"] += 35
            if statok["energia"] > 100:
                statok["energia"] = 100

            statok["kaja"] -= 25

        case 2:
            event = choices(
                ["ferfi", "nok", "biztHiba", "vezetekSzakadas", "semmi"],
                weights=[15, 15, 35, 5, 30],
            )
            match event[0]:
                case "semmi":
                    await print_szoveg(["Semmi érdekes nem történik..."], False)

                case "ferfi":
                    await print_szoveg(read("eventek vonat ferfi"), False)
                    statok["energia"] -= 10

                case "nok":
                    await print_szoveg(read("eventek vonat nok"), False)
                    statok["energia"] -= 25

                case "biztHiba":
                    await print_szoveg(read("eventek vonat biztHiba"), False)
                    add_time(40)

                case "vezetekSzakadas":
                    await print_szoveg(read("eventek vonat vezetekSzakadas"), False)
                    add_time(120)

    add_time(120)
    return "allomas"


async def bolt_menu() -> list:
    global statok
    global inventory
    global energiaital_ar
    global sportszelet_ar
    global fank_ar
    global rozsa_ar

    update_opciok(
        [
            f"Energiaital vásárlás ({energiaital_ar} Ft)",
            f"Sportszelet vásárlás ({sportszelet_ar} Ft)",
            f"Fánk vásárlás ({fank_ar} Ft)",
            f"Virág vásárlás ({rozsa_ar} Ft)",
            "Virág lopás",
            "Étel lopás",
            "Séta az állomásra",
            "Futás az állomásra",
        ]
    )
    x = await waitforkey(["1", "2", "3", "4", "5", "6", "7", "8"])
    penz = statok["penz"]
    match x:
        case 1:
            if penz - energiaital_ar >= 0:
                inventory["Energiaital"] += 1
                statok["penz"] -= energiaital_ar
                update_stats()
                await print_szoveg(["Vettél egy Energiaitalt."], True)
                if statok["varos"] == "Tatabánya":
                    await sleep(1)
                    statok["rozsa"] = True
                    await print_szoveg(read("allomasok becs dancika"), False)
                    await print_szoveg(read("allomasok becs gazdag"), False)
                    await print_szoveg(read("allomasok becs temetes"), False)
                    exit(0)
            else:
                await print_szoveg(read("menu bolt nincsPenz"), True)

        case 2:
            if penz - sportszelet_ar >= 0:
                inventory["Sportszelet"] += 1
                statok["penz"] -= sportszelet_ar
                update_stats()
                await print_szoveg(["Vettél egy sportszeletet."], True)
            else:
                await print_szoveg(read("menu bolt nincsPenz"), True)

        case 3:
            if penz - fank_ar >= 0:
                inventory["Fánk"] += 1
                statok["penz"] -= fank_ar
                update_stats()
                await print_szoveg(["Vettél egy fánkot."], True)
            else:
                await print_szoveg(read("menu bolt nincsPenz"), True)

        case 4:
            if statok["rozsa"] == False:
                if penz - rozsa_ar >= 0:
                    statok["rozsa"] = True
                    statok["penz"] -= rozsa_ar
                    update_stats()
                    await print_szoveg(["Vettél egy rózsát."], True)
                else:
                    await print_szoveg(read("menu bolt nincsPenz"), True)
            else:
                await print_szoveg(["Már van virágod."], True)

        case 5:
            if statok["rozsa"] == False:
                await print_szoveg(["Úgy döntesz, hogy lopsz egy virágot."], False)
                x = choices(["elkap", "nemElkap"], weights=[60, 40])
                if x[0] == "elkap":
                    await print_szoveg(read("menu bolt elkapnak"), False)
                    exit(0)

                statok["rozsa"] = True
                update_stats()
                await print_szoveg(read("menu bolt lopas"), False)
            else:
                await print_szoveg(["Már van virágod."], True)

        case 6:
            await print_szoveg(["Úgy döntesz, hogy lopsz egy sportszeletet."], False)
            x = choices(["elkap", "nemElkap"], weights=[20, 80])
            if x[0] == "elkap":
                await print_szoveg(read("menu bolt elkapnak"), False)
                exit(0)

            inventory["Sportszelet"] += 1
            update_stats()
            await print_szoveg(read("menu bolt lopas"), False)

        case 7:
            statok["energia"] -= 15
            add_time(60)
            sleep(0.01)
            if statok["energia"] <= 0:
                statok["energia"] = 0
                update_stats()
                await print_szoveg(read("meghalt energia"), False)
                exit(0)
            event = choices(
                ["rablas", 500, 200, 50, 10, "semmi"], weights=[7, 8, 12, 18, 20, 35]
            )
            match event[0]:
                case "semmi":
                    await print_szoveg(read("menu bolt seta"), True)

                case 500:
                    await print_szoveg(["Elkezdesz sétálni az állomás felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=500)
                    statok["penz"] += 500
                    update_stats()

                case 200:
                    await print_szoveg(["Elkezdesz sétálni az állomás felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=200)
                    statok["penz"] += 200
                    update_stats()

                case 50:
                    await print_szoveg(["Elkezdesz sétálni az állomás felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=50)
                    statok["penz"] += 50
                    update_stats()

                case 10:
                    await print_szoveg(["Elkezdesz sétálni az állomás felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=10)
                    statok["penz"] += 10
                    update_stats()

                case "rablas":
                    szazalek = randint(15, 50) / 100
                    penz = statok["penz"]
                    elveszt = penz - penz * szazalek
                    await print_szoveg(["Elkezdesz sétálni az állomás felé..."], False)
                    await print_szoveg(
                        read("eventek varos rablas"), True, penz=int(penz - elveszt)
                    )
                    statok["penz"] -= int(elveszt)
                    update_stats(statok)
                    add_time(15)

            return "allomas"

        case 8:
            statok["energia"] -= 30
            add_time(30)
            sleep(0.01)
            if statok["energia"] <= 0:
                statok["energia"] = 0
                update_stats()
                await print_szoveg(read("meghalt energia"), False)
                exit(0)
            event = choices(
                ["rablas", 500, 200, 50, 10, "semmi"], weights=[10, 5, 12, 18, 20, 35]
            )
            match event[0]:
                case "semmi":
                    await print_szoveg(read("menu bolt futas"), True)

                case 500:
                    statok["penz"] += 500
                    update_stats()
                    await print_szoveg(["Elkezdesz futni az állomás felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=500)

                case 200:
                    statok["penz"] += 200
                    update_stats()
                    await print_szoveg(["Elkezdesz futni az állomás felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=200)

                case 50:
                    statok["penz"] += 50
                    update_stats()
                    await print_szoveg(["Elkezdesz futni az állomás felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=50)

                case 10:
                    statok["penz"] += 10
                    update_stats()
                    await print_szoveg(["Elkezdesz futni az állomás felé..."], False)
                    await print_szoveg(read("eventek varos penz"), True, penz=10)

                case "rablas":
                    szazalek = randint(15, 50) / 100
                    penz = statok["penz"]
                    elveszt = penz - penz * szazalek
                    statok["penz"] -= int(elveszt)
                    update_stats(statok)
                    await print_szoveg(["Elkezdesz sétálni az állomás felé..."], False)
                    await print_szoveg(
                        read("eventek varos rablas"), True, penz=int(penz - elveszt)
                    )
                    add_time(15)

            return "allomas"


async def waitforkey(allowed: list | str) -> int | None:
    global pressed
    pressed = "default"
    global allowed_list
    allowed_list = allowed

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while True:
        if pressed != "default":
            listener.stop()
            return pressed


def on_press(key):
    global statok
    global inventory
    global pressed
    global allowed_list
    allowed = allowed_list

    if key == keyboard.Key.esc:
        return False

    try:
        k = key.char
    except:
        k = key.name

    update_stats()
    match k:
        case "q":
            if inventory["Fánk"] >= 1:
                inventory["Fánk"] -= 1
                if 100 <= (statok["kaja"] + 50):
                    statok["kaja"] = 100
                else:
                    statok["kaja"] += 50

        case "w":
            if inventory["Sportszelet"] >= 1:
                inventory["Sportszelet"] -= 1
                if 100 <= (statok["kaja"] + 35):
                    statok["kaja"] = 100
                else:
                    statok["kaja"] += 35
                if 100 <= (statok["energia"] + 20):
                    statok["energia"] = 100
                else:
                    statok["energia"] += 20

        case "e":
            if inventory["Energiaital"] >= 1:
                inventory["Energiaital"] -= 1
                statok["energia"] = 100

        case _:
            if type(allowed) == list and k in allowed:
                pressed = int(k)
                return False

            elif type(allowed) == str:
                pressed = None
                return False


async def tick():
    global ido
    global statok
    while True:
        await sleep(1)
        ido += datetime.timedelta(minutes=1)
        update_stats()
        statok["energia"] -= 0.2
        statok["kaja"] -= 0.2

        if statok["energia"] <= 0:
            statok["energia"] = 0
            update_stats()
            await print_szoveg(read("meghalt energia"), False)
            exit(0)

        if statok["kaja"] <= 0:
            statok["kaja"] = 0
            update_stats()
            await print_szoveg(read("meghalt ehseg"), False)
            exit(0)


def time():
    return ido


def set_time(hour: int, minute: int):
    global ido
    ido = datetime.datetime(
        year=ido.year, month=ido.month, day=ido.day, hour=hour, minute=minute
    )


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
            layout["szoveg"].update(
                Padding(Align(string, "center", vertical="middle"), 2)
            )
            await asyncio.sleep(0.01)

        if tovabb:
            if i != len(szovegz) - 1:
                await waitforkey("space")
        else:
            await waitforkey("space")


def set_kovetkezo_vonat(input: list):
    global kovetkezo_vonat
    kovetkezo_vonat = input


def nemElkesett() -> bool:
    if ido.day == 1:
        return True
    if ido.hour >= 15:
        return False
    else:
        return True


live = Live(layout, auto_refresh=True, refresh_per_second=60)
