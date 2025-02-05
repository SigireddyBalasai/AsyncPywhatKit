from platform import system
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
__version__ = "2.2.7.2"
_system = system().lower()
if _system in ("darwin", "windows"):
    from .misc import take_screenshot