import asyncio
import os
from AsyncPywhatKit.src import sendwhatsdoc_immediately

print(os.path.abspath("/Core/data/document.png"))


async def main():
    await  sendwhatsdoc_immediately("+91 9398993400",
                                    'C:\\Users\\sigir\\PycharmProjects\\AsyncPywhatKit\\AsyncPywhatKit\\src\\whats.py')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
