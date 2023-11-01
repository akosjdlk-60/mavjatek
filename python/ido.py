import datetime
from asyncio import sleep

async def clock():
    global ido
    ido = datetime.datetime(year=2023, month=1, day=1, hour=8, minute=0)
    while True:
        await sleep(1)
        ido += datetime.timedelta(minutes=1)

def time():
    return ido

def set_time(hour:int, minute:int):
    global ido
    ido = datetime.datetime(year=ido.year, month=ido.month, day=ido.day, hour=hour, minute=minute)


def add_time(change: int):
    """
    change: Hány perc időt adjunk hozzá.
    """
    global ido
    ido += datetime.timedelta(minutes=change)    
    