import asyncio
import os
from AsyncPywhatKit.src.Core.core import find_link

print(os.path.abspath("/Core/data/document.png"))


async def main():
    while True:
        try:
            ok = await find_link()
            print(ok)
        except:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
