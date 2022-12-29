import asyncio
import AsyncPywhatKit
import os
from re import fullmatch
from AsyncPywhatKit import sendimg_or_video_immediately, sendwhatsdoc_immediately

print(os.path.abspath("/Core/data/document.png"))


async def main():
    await sendimg_or_video_immediately("+91 9398993400", ['AsyncPywhatKit/Core/data/document.png','AsyncPywhatKit/Core/data/link.png'])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
