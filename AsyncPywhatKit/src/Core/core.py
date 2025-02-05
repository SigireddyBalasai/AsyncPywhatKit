import asyncio
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from platform import system
from urllib.parse import quote
from webbrowser import open
from pathlib import Path
import aiohttp
from pyautogui import click, hotkey, moveTo, press, size, typewrite
from pyscreeze import screenshot
import cv2
import numpy as np

from .exceptions import InternetException, ImageNotFoundException

WIDTH, HEIGHT = size()

Box = collections.namedtuple('Box', 'left top width height score')





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
    dir_path = Path(__file__).resolve().parent
    search_bar_path = dir_path / "data" / "searchbar.png"
    location = locateOnScreen(str(search_bar_path))
    try:
        moveTo(location[0] + location[2] / 2, location[1] + location[3])
        click()
    except:
        search_bar_path = dir_path / "data" / "searchbar2.png"
        location = locateOnScreen(str(search_bar_path))
        moveTo(location[0] + location[2] / 2, location[1] + location[3])
        click()


async def find_textbox() -> None:
    """Click on text box"""
    dir_path = Path(__file__).resolve().parent
    text_box_path = dir_path / "data" / "pywhatkit_smile.png"
    location = locateOnScreen(str(text_box_path))
    try:
        moveTo(location[0] + 150, location[1] + 5)
        click()
    except:
        text_box_path = dir_path / "data" / "pywhatkit_smile1.png"
        location = locateOnScreen(str(text_box_path))
        moveTo(location[0] + 150, location[1] + 5)
        click()


async def find_link():
    dir_path = Path(__file__).resolve().parent
    link_paths = ["link.png", "link2.png"]
    locations = [locateOnScreen(str(dir_path / "data" / loc), grayscale=True, confidence=0.9, multiscale=True) for loc in link_paths]
    location = max(locations, key=lambda loc: loc[1] if loc else 0)
    if location:
        moveTo(location[0] + location[2] / 2, location[1] + location[3] / 2)
        click()


async def find_document():
    dir_path = Path(__file__).resolve().parent
    document_path = dir_path / "data" / "document.png"
    location = locateOnScreen(str(document_path), confidence=0.8, multiscale=True, grayscale=True)
    if location:
        moveTo(location[0] + location[2] / 2, location[1] + location[3] / 2)
        click()


async def find_photo_or_video():
    dir_path = Path(__file__).resolve().parent
    photo_path = dir_path / "data" / "photo_or_video.png"
    location = locateOnScreen(str(photo_path), confidence=0.8, multiscale=True, grayscale=True)
    if location:
        moveTo(location[0] + location[2] / 2, location[1] + location[3] / 2)
        click()


async def check_connection() -> None:
    """Check the Internet connection of the Host Machine"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://google.com") as response:
                if response.status >= 400:
                    raise InternetException("Error while connecting to the Internet.")
    except:
        raise InternetException("Error while connecting to the Internet. Make sure you are connected to the Internet!")


async def _web(receiver: str, message: str) -> None:
    """Opens WhatsApp Web based on the Receiver"""
    if await check_number(receiver):
        open(f"https://web.whatsapp.com/send?phone={receiver}&text={quote(message)}")
    else:
        open(f"https://web.whatsapp.com/accept?code={receiver}")


async def send_message(message: str, receiver: str, wait_time: int) -> None:
    """Parses and Sends the Message"""
    await _web(receiver, message)
    await asyncio.sleep(7)
    click(WIDTH / 2, HEIGHT / 2 + 15)
    await asyncio.sleep(wait_time - 7)
    await _web(receiver, message)
    await asyncio.sleep(7)
    click(WIDTH / 2, HEIGHT / 2)
    await asyncio.sleep(wait_time - 7)
    if not await check_number(receiver):
        for char in message:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
    await find_textbox()
    press("enter")


def locateOnScreen(image: str, **kwargs) -> Box:
    """Locate button on screen using cv2.TemplateMatching algorithm"""
    screenshot_im = screenshot(region=None)
    box_result = locateMax_opencv(image, screenshot_im, **kwargs)
    try:
        screenshot_im.fp.close()
    except AttributeError:
        pass
    return box_result


def locateMax_opencv(template: str, screen_image: str, grayscale: bool = False, confidence: float = 0.9, multiscale: bool = False) -> Box:
    """Locate button using cv2.TemplateMatching algorithm"""
    template = loadImage(template, grayscale)
    template_h, template_w = template.shape[:2]
    screen_image = loadImage(screen_image, grayscale)

    if screen_image.shape[0] < template.shape[0] or screen_image.shape[1] < template.shape[1]:
        raise ValueError('needle dimension(s) exceed the haystack image or region dimensions')

    if multiscale:
        sizes = [1, 0.9, 0.85, 0.8]
        match_x, match_y = None, None
        with ThreadPoolExecutor() as executor:
            future_to_contour = {executor.submit(cv2.matchTemplate, screen_image.copy(), cv2.resize(template.copy(), (0, 0), fx=size, fy=size), cv2.TM_CCORR_NORMED): size for size in sizes}
            for future in as_completed(future_to_contour):
                _, max_val, _, max_loc = cv2.minMaxLoc(future.result())
                if max_val >= confidence:
                    confidence = max_val
                    match_x = max_loc[0]
                    match_y = max_loc[1]
        if match_x is not None:
            return Box(match_x, match_y, template_w, template_h, max_val)
        raise ImageNotFoundException

    result = cv2.matchTemplate(screen_image, template, cv2.TM_CCORR_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        match_x = max_loc[0]
        match_y = max_loc[1]
        return Box(match_x, match_y, template_w, template_h, max_val)
    raise ImageNotFoundException


def loadImage(img_to_load: str, gray: bool) -> np.ndarray:
    if not os.path.exists(img_to_load):
        raise FileNotFoundError(f"Image not found: {img_to_load}")
    image = cv2.imread(img_to_load)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if gray else image
