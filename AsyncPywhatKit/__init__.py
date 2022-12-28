from platform import system

from AsyncPywhatKit.ascii_art import image_to_ascii_art
from AsyncPywhatKit.handwriting import text_to_handwriting
from AsyncPywhatKit.mail import send_hmail, send_mail
from AsyncPywhatKit.misc import info, playonyt, search, show_history, take_screenshot
from AsyncPywhatKit.sc import cancel_shutdown, shutdown
from AsyncPywhatKit.whats import (
    open_web,
    sendwhatmsg,
    sendwhatmsg_instantly,
    sendwhatmsg_to_group,
    sendwhatmsg_to_group_instantly,
    sendimg_or_video_immediately,
    sendwhatsmsg_to_all,
    sendwhatdoc_immediately
)

_system = system().lower()
if _system in ("darwin", "windows"):
    from AsyncPywhatKit.misc import take_screenshot

if _system == "windows":
    from AsyncPywhatKit.remotekit import start_server