import keyboard


async def waitforkey(key: list | str) -> str | None:
    """
    list -> str: melyik key lett eloszor lenyomva\n
    str -> None: var amig le nem lett nyomva majd tovabblep (semmit nem csinal)
    """
    while True:
        event = keyboard.read_event(suppress=True)
        if type(key) == list:
            for i in range(len(key)):
                if event.name == key[i]:
                    return event.name
        elif type(key) == str and event.name == key:
            return None
            

        

async def hotkeys():
    def print_pressed_keys(e: keyboard.KeyboardEvent):
        print(e.name)
	
    keyboard.on_release(print_pressed_keys, suppress=True)