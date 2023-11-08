from os import system as cmd
cmd("pip install -r requirements.txt")

from python.main import main
import asyncio
asyncio.run(main())