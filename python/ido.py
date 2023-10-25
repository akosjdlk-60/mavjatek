import datetime
from asyncio import sleep

async def clock():
    global ido
    ido = datetime.time(8,0)
    while True:
        sleep(1)
        ido += datetime.timedelta(minutes=1)

def time():
    return ido
    
        