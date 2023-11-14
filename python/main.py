import asyncio
import keyboard
import menuk as menuk
from dialogue_parser import read

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
    
    while True: #soha nem lepunk ki

        while menuk.get_info()[0]["varos"] != "Bécs":
            
            while True:
                match menuk.get_info()[0]["varos"]:

                    case "Tatabánya":
                        pass

                    case "Győr":
                        pass
                    
                x = await menuk.allomas_menu()
                match x:

                    case "bolt":
                        bolt = await menuk.bolt_menu()
                        match bolt:
                            
                            case "1":
                                pass

                    case "allomas":
                        break

                    case "vonat":
                        vonat = await menuk.vonat_menu()

        #bécs cuccos
        
        
asyncio.run(main())