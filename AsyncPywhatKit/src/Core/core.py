import asyncio
import os
from platform import system
from urllib.parse import quote
from webbrowser import open

import aiohttp
from pyautogui import click, hotkey, locateOnScreen, moveTo, press, size, typewrite

from .exceptions import InternetException

WIDTH, HEIGHT = size()


async def check_number(number: str) -> bool:
    """Checks if the Number is Valid or not"""

    return "+" in number or "_" in number


async def close_tab(wait_time: int = 2) -> None:
    """Closes the Currently Opened Browser Tab"""

    await asyncio.sleep(wait_time)
    _system = system().lower()
    if _system in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif _system == "darwin":
        hotkey("command", "w")
    else:
        raise Warning(f"{_system} not supported!")
    press("enter")


def find_recent_chat():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\searchbar.png")
    try:
        moveTo(location[0] + location[2] / 2, location[1] + location[3])
        click()
    except:
        location = locateOnScreen(f"{dir_path}\\data\\searchbar2.png")
        moveTo(location[0] + location[2] / 2, location[1] + location[3])
        click()


async def findtextbox() -> None:
    """click on text box"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\pywhatkit_smile1.png")
    try:
        moveTo(location[0] + 150, location[1] + 5)
        click()
    except:
        location = locateOnScreen(f"{dir_path}\\data\\pywhatkit_smile.png")
        moveTo(location[0] + 150, location[1] + 5)
        click()


async def find_link():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        location = locateOnScreen(f"{dir_path}\\data\\link.png")
        moveTo(location[0] + location[2] / 2, location[1] + location[3] / 2)
        click()
    except Exception:
        location = locateOnScreen(f"{dir_path}\\data\\link2.png")
        moveTo(location[0] + location[2] / 2, location[1] + location[3] / 2)
        print(location)
        click()


async def find_document():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\document.png")
    print(location)
    moveTo(location[0] + location[2] / 2, location[1] + location[3] / 2)
    click()


async def find_photo_or_video():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\photo_or_video.png")
    print(location)
    moveTo(location[0] + location[2] / 2, location[1] + location[3] / 2)
    click()


async def check_connection() -> None:
    """Check the Internet connection of the Host Machine"""

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://google.com") as response:
                status = response.status
                if status < 400:
                    pass

    except:
        raise InternetException(
            "Error while connecting to the Internet. Make sure you are connected to the Internet!"
        )


async def _web(receiver: str, message: str) -> None:
    """Opens WhatsApp Web based on the Receiver"""
    if check_number(number=receiver):
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)


async def send_message(message: str, receiver: str, wait_time: int) -> None:
    """Parses and Sends the Message"""

    await _web(receiver=receiver, message=message)
    await asyncio.sleep(7)
    click(WIDTH / 2, HEIGHT / 2 + 15)
    await asyncio.sleep(wait_time - 7)
    await _web(receiver=receiver, message=message)
    await asyncio.sleep(7)
    click(WIDTH / 2, HEIGHT / 2)
    await asyncio.sleep(wait_time - 7)
    if not check_number(number=receiver):
        for char in message:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
    await findtextbox()
    press("enter")
