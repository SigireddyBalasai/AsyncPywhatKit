import asyncio
import os
from AsyncPywhatKit import sendimg_or_video_immediately

print(os.path.abspath("/Core/data/document.png"))


async def main():
    await sendimg_or_video_immediately("+91 9398993400", ['AsyncPywhatKit/Core/data/document.png','AsyncPywhatKit/Core/data/link.png'])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
