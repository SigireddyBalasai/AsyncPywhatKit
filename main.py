import asyncio
import AsyncPywhatKit

from re import fullmatch

print(not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", "+919398993400"))


async def main():
    """maim"""
    await AsyncPywhatKit.sendwhatdoc_immediately("+91 9398993400",
                                                      "C:\\Users\\sigir\\AsyncPywhatKit\\AsyncPywhatKit\\Core\\data\\document.png")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
