import asyncio
import sys
import os
sys.path.insert(0, f'{os.path.abspath(os.getcwd())}\\python')
import menuk
from dialogue_parser import read
varos = 2
varos_refresh = False
async def main():
    global varos
    global varos_refresh
    await asyncio.sleep(0.01)
    await menuk.load()
    
    while True: #soha nem lepunk ki

        while menuk.get_info()[0]["varos"] != "Bécs":
            
            while True:
                if varos_refresh == True:
                    match varos:

                        case 2:
                            await menuk.print_szoveg(read("allomasok tatabanya"), False)
                            menuk.set_kovetkezo_vonat([7, 15])
                            varos_refresh = False
                            statok = menuk.get_stats()
                            statok["varos"] = "Tatabánya"
                            statok["keregetett"] = True
                            menuk.update_stats(statok=statok)
                            varos += 1

                        case 3:
                            await menuk.print_szoveg(read("allomasok gyor"), False)
                            menuk.set_kovetkezo_vonat([12, 10])
                            varos_refresh = False
                            statok = menuk.get_stats()
                            statok["varos"] = "Győr"
                            statok["keregetett"] = True
                            menuk.update_stats(statok=statok)
                            varos += 1               

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
        statok["varos"] = "Tatabánya"
        menuk.update_stats(statok=statok)
        varos += 1

        await menuk.print_szoveg(read("allomasok becs erkezes"), False)
        if menuk.get_info()[0]["rozsa"]:
            await menuk.print_szoveg(read("allomasok becs gazdag"), False)
            await menuk.print_szoveg(read("allomasok becs temetes"), False)
        else:
            await menuk.print_szoveg(read("allomasok becs viragNincs"), False)
            await menuk.print_szoveg(read("allomasok becs kitagadnak"), False)
            await menuk.print_szoveg(read("allomasok becs temetes"), False)
        exit(0)
        
        
        
asyncio.run(main())