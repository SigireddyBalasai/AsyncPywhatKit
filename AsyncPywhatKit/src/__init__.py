from platform import system

from .ascii_art import image_to_ascii_art
from .handwriting import text_to_handwriting
from .mail import send_hmail, send_mail
from .misc import info, playonyt, search, show_history, take_screenshot
from .sc import cancel_shutdown, shutdown
from .Core import core,exceptions,log
from .whats import (
    open_web,
    sendwhatmsg,
    sendwhatmsg_instantly,
    sendwhatmsg_to_group,
    sendwhatmsg_to_group_instantly,
    sendimg_or_video_immediately,
    sendwhatsmsg_to_all,
    sendwhatsdoc_immediately
)

_system = system().lower()
if _system in ("darwin", "windows"):
    from .misc import take_screenshot

if _system == "windows":
    from .remotekit import start_server