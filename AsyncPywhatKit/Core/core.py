import asyncio
import os
import pathlib
import time
import webbrowser
from platform import system
from urllib.parse import quote
from webbrowser import open
import time

import aiohttp
from pyautogui import click, hotkey, locateOnScreen, moveTo, press, size, typewrite

from AsyncPywhatKit.Core.exceptions import InternetException

WIDTH, HEIGHT = size()


async def check_number(number: str) -> bool:
    """Checks the Number to see if contains the Country Code"""

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
        moveTo(location[0]+location[2]/2,location[1]+location[3])
        click()
    except:
        location = locateOnScreen(f"{dir_path}\\data\\searchbar2.png")
        moveTo(location[0]+location[2]/2,location[1]+location[3])
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
    location = locateOnScreen(f"{dir_path}\\data\\link.png")
    print(location)
    try:
        moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
        click()
    except Exception:
        location = locateOnScreen(f"{dir_path}\\data\\link2.png")
        moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
        print(location)
        click()
async def find_document():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\document.png")
    print(location)
    moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
    click()

async def find_photo_or_video():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\photo_or_video.png")
    print(location)
    moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
    click()


async def check_connection() -> None:
    """Check the Internet connection of the Host Machine"""

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://google.com") as response:
                status = response.status
                if status < 400:
                    pass

    except :
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


async def copy_image(path: str) -> None:
    """Copy the Image to Clipboard based on the Platform"""

    _system = system().lower()
    if _system == "linux":
        if pathlib.Path(path).suffix in (".PNG", ".png"):
            os.system(f"copyq copy image/png - < {path}")
        elif pathlib.Path(path).suffix in (".jpg", ".JPG", ".jpeg", ".JPEG"):
            os.system(f"copyq copy image/jpeg - < {path}")
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    elif _system == "windows":
        from io import BytesIO

        import win32clipboard  # pip install pywin32
        from PIL import Image

        image = Image.open(path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
    elif _system == "darwin":
        if pathlib.Path(path).suffix in (".jpg", ".jpeg", ".JPG", ".JPEG"):
            os.system(
                f"osascript -e 'set the clipboard to (read (POSIX file \"{path}\") as JPEG picture)'"
            )
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    else:
        raise Exception(f"Unsupported System: {_system}")


async def send_image(path: str, caption: str, receiver: str, wait_time: int) -> None:
    """Sends the Image to a Contact or a Group based on the Receiver"""

    await _web(message=caption, receiver=receiver)
    await asyncio.sleep(7)
    click(WIDTH / 2, HEIGHT / 2 + 15)
    await asyncio.sleep(wait_time - 7)
    await copy_image(path=path)
    await _web(message=caption, receiver=receiver)
    await asyncio.sleep(7)
    click(WIDTH / 2, HEIGHT / 2)
    await asyncio.sleep(wait_time - 7)
    await copy_image(path=path)
    if not check_number(number=receiver):
        for char in caption:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
    else:
        typewrite(" ")
    if system().lower() == "darwin":
        hotkey("command", "v")
    else:
        hotkey("ctrl", "v")
    await asyncio.sleep(1)
    await findtextbox()
    press("enter")
webbrowser.open("https://web.whatsapp.com/")
time.sleep(10)
dir_path = os.path.dirname(os.path.realpath(__file__))
location = locateOnScreen(f"{dir_path}\\data\\searchbar.png")
print(location)
moveTo(location[0] + location[2] / 2, location[1] + location[3] / 2)
