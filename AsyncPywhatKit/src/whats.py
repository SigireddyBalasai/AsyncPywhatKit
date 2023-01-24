import time
import webbrowser as web
from datetime import datetime
from re import fullmatch
from typing import List
from urllib.parse import quote
import pyperclip
import keyboard
import pathlib
import pyautogui as pg
import asyncio
from .Core import core, log, exceptions

pg.FAILSAFE = False


async def main():
    """Check the internet connection."""
    await core.check_connection()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


async def sendwhatmsg_instantly(
        phone_no: str,
        message: str,
        wait_time: int = 15,
        tab_close: bool = True,
        close_time: int = 3
) -> None:
    """Send a WhatsApp message instantly.
    
    This function opens a new tab in the default web browser, navigates to the WhatsApp web page, and sends a message to the specified phone number.
    
    Parameters:
    message: The message to be sent.
    phone_no: The phone number to send the message to.
    wait_time: The time to wait before sending the message (in seconds).
    tab_close: A flag indicating whether to close the tab after sending the message.
    close_time: The time to wait before closing the tab (in seconds).
    
    Returns:
    None.
    """
    print(phone_no)
    print(await core.check_number(number=phone_no))
    if not await core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")
    phone_no = phone_no.replace(" ", "")
    print(phone_no)
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")
    phone_no = phone_no.replace(" ", "")
    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}", new=0)
    await asyncio.sleep(wait_time)
    pg.press('enter')
    await asyncio.sleep(close_time)
    if tab_close:
        await core.close_tab(wait_time=close_time)


async def sendwhatmsg(
        phone_no: str = None,
        message: str = None,
        time_hour: int = None,
        time_min: int = None,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send a WhatsApp message at a certain time.
    
    This function schedules the sending of a WhatsApp message to a specified phone number at a specified time.
    
    Parameters:
    phone_no: The phone number to send the message to.
    message: The message to be sent.
    time_hour: The hour at which to send the message (in 24-hour format).
    time_min: The minute at which to send the message.
    wait_time: The time to wait before sending the message (in seconds).
    tab_close: A flag indicating whether to close the tab after sending the message.
    close_time: The time to wait before closing the tab (in seconds).
    
    Returns:
    None.
    """
    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    await asyncio.sleep(sleep_time)
    await sendwhatmsg_instantly(message, phone_no)
    if tab_close:
        await core.close_tab(wait_time=close_time)


async def sendwhatmsg_to_group(
        group_id: str,
        message: str,
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send a WhatsApp message to a group at a certain time.
    
    This function schedules the sending of a WhatsApp message to a specified group at a specified time.
    
    Parameters:
    group_id: The ID of the group to send the message to.
    message: The message to be sent.
    time_hour: The hour at which to send the message (in 24-hour format).
    time_min: The minute at which to send the message.
    wait_time: The time to wait before sending the message (in seconds).
    tab_close: A flag indicating whether to close the tab after sending the message.
    close_time: The time to wait before closing the tab (in seconds).
    
    Returns:
    None.
    """
    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    await asyncio.sleep(sleep_time)
    await sendwhatmsg_instantly(group_id, message)
    await log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        await core.close_tab(wait_time=close_time)


async def sendwhatmsg_to_group_instantly(
        group_id: str,
        message: str,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send a WhatsApp message to a group instantly.
    
    This function opens the WhatsApp Web page in a new tab and sends a message to the specified group.
    
    Parameters:
    group_id: The ID of the group to send the message to.
    message: The message to be sent.
    wait_time: The time to wait before sending the message (in seconds).
    tab_close: A flag indicating whether to close the tab after sending the message.
    close_time: The time to wait before closing the tab (in seconds).
    
    Returns:
    None.
    """
    current_time = time.localtime()
    await asyncio.sleep(4)
    await sendwhatmsg_instantly(group_id, message)
    await log.log_message(_time=current_time, receiver=group_id, message=message)

    if tab_close:
        await core.close_tab(wait_time=close_time)


async def sendwhatsmsg_to_all(
        phone_nos: List[str],
        message: str,
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send a WhatsApp message to a list of phone numbers at a certain time.
    
    This function schedules the sending of a WhatsApp message to a list of specified phone numbers at a specified time.
    
    Parameters:
    phone_nos: The list of phone numbers to send the message to.
    message: The message to be sent.
    time_hour: The hour at which to send the message (in 24-hour format).
    time_min: The minute at which to send the message.
    wait_time: The time to wait before sending the message (in seconds).
    tab_close: A flag indicating whether to close the tab after sending the message.
    close_time: The time to wait before closing the tab (in seconds).
    
    Returns:
    None.
    """
    for phone_n in phone_nos:
        await sendwhatmsg(
            phone_n, message, time_hour, time_min, wait_time, tab_close, close_time
        )


async def sendimg_or_video_immediately(
        phone_no: str,
        path: str,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send an image or video file via WhatsApp instantly.
    
    This function opens a new tab in the default web browser, navigates to the WhatsApp web page, and sends an image or video file to the specified phone number.
    
    Parameters:
    phone_no: The phone number to send the file to.
    path: The file path of the image or video file to be sent.
    wait_time: The time to wait before sending the file (in seconds).
    tab_close: A flag indicating whether to close the tab after sending the file.
    close_time: The time to wait before closing the tab (in seconds).
    
    Returns:
    None.
    """

    if not await core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    await core.find_link()
    time.sleep(1)
    await core.find_photo_or_video()
    if type(path) == str:
        path = pathlib.Path(path)
        pyperclip.copy(str(path.resolve()))
        print("Copied")
    else:
        strn = []
        for paths in path:
            patha = str(pathlib.Path(paths).resolve())
            strn.append(f'"{patha}"')

        print(" ".join(strn))
        pyperclip.copy(" ".join(strn))
    time.sleep(1)
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    if tab_close:
        await core.close_tab(wait_time=close_time)


async def sendwhatsdoc_immediately(
        phone_no: str,
        path: str,
        wait_time: int = 15,
        tab_close: bool = True,
        close_time: int = 3,
) -> None:
    """Send a WhatsApp document instantly.

This function opens a new tab in the default web browser, navigates to the WhatsApp web page, and sends a document to the specified phone number.

Parameters:
phone_no: The phone number to send the document to.
path: The file path of the document to be sent.
wait_time: The time to wait before sending the document (in seconds).
tab_close: A flag indicating whether to close the tab after sending the document.
close_time: The time to wait before closing the tab (in seconds).

Returns:
None.
"""

    if not await core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    await core.find_link()
    time.sleep(1)
    await core.find_document()
    if type(path) == str:
        path = pathlib.Path(path)
        pyperclip.copy(str(path.resolve()))
        print("Copied")
    else:
        strn = []
        for paths in path:
            patha = str(pathlib.Path(paths).resolve())
            strn.append(f'"{patha}"')

        print(" ".join(strn))
        pyperclip.copy(" ".join(strn))

    time.sleep(1)
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    if tab_close:
        await core.close_tab(wait_time=close_time)


def open_web() -> bool:
    """Opens WhatsApp Web """

    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True
