import asyncio
import sys
from random import choices
import os

sys.path.insert(0, f"{os.path.abspath(os.getcwd())}\\python")
import menuk
from dialogue_parser import read

varos = 1
varos_refresh = False


async def main():
    global varos
    global varos_refresh
    await asyncio.sleep(0.01)
    await menuk.load()

    while True:  # soha nem lepunk ki
        while menuk.get_stats()['varos'] != "Bécs":
            while True:
                if varos_refresh == True:
                    match varos:
                        case 1:
                            varos_refresh = False
                            await menuk.print_szoveg(read("allomasok tatabanya"), False)
                            menuk.set_kovetkezo_vonat([7, 15])
                            statok = menuk.get_stats()
                            statok["varos"] = "Tatabánya"
                            statok["keregetett"] = False
                            menuk.update_stats(statok=statok)
                            varos += 1

                        case 2:
                            varos_refresh = False
                            await menuk.print_szoveg(read("allomasok gyor"), False)
                            menuk.set_kovetkezo_vonat([12, 10])
                            statok = menuk.get_stats()
                            statok["varos"] = "Győr"
                            statok["keregetett"] = False
                            menuk.update_stats(statok=statok)
                            varos += 1
                        case 3:
                            varos_refresh = False
                            statok = menuk.get_stats()
                            statok["varos"] = "Bécs"
                            statok["keregetett"] = False
                            menuk.update_stats(statok=statok)
                            await menuk.print_szoveg(
                                read("allomasok becs erkezes"), False
                            )
                            x = choices(["elut", "nemElut"], weights=[30, 70])
                            if x[0] == "nemElut":
                                if menuk.get_stats()["rozsa"]:
                                    await menuk.print_szoveg(
                                        read("allomasok becs gazdag"), False
                                    )
                                    await menuk.print_szoveg(
                                        read("allomasok becs temetes"), False
                                    )
                                else:
                                    await menuk.print_szoveg(
                                        read("allomasok becs viragNincs"), False
                                    )
                                    await menuk.print_szoveg(
                                        read("allomasok becs kitagadnak"), False
                                    )
                                    await menuk.print_szoveg(
                                        read("allomasok becs temetes"), False
                                    )
                                exit(0)
                            await menuk.print_szoveg(
                                read("allomasok becs vonatElut"), False
                            )
                            await menuk.print_szoveg(
                                read("allomasok becs temetes"), False
                            )
                            exit(0)

                while True:
                    allomas = await menuk.allomas_menu()
                    match allomas:
                        case "bolt":
                            while True:
                                bolt = await menuk.bolt_menu()
                                match bolt:
                                    case "allomas":
                                        break

                        case "allomas":
                            continue

                        case "vonat":
                            vonat = await menuk.vonat_menu()

                            match vonat:
                                case "allomas":
                                    varos_refresh = True
                                    break

        statok = menuk.get_stats()
        menuk.update_stats(statok=statok)
        varos += 1


asyncio.run(main())
