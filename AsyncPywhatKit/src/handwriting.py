import aiohttp

from AsyncPywhatKit.src.Core import exceptions


async def text_to_handwriting(
    string: str, save_to: str = "pywhatkit.png", rgb: tuple = (0, 0, 0)
) -> None:
    """Convert the given String to Handwritten Characters"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://pywhatkit.herokuapp.com/handwriting?text={string}&rgb={rgb[0]},{rgb[1]},{rgb[2]}") as response:
            status_code = response.status
            if status_code == 200:
                with open(save_to, "wb") as file:
                    file.write(await response.read())
                    file.close()
            elif 400 <= status_code <= 599:
                raise exceptions.UnableToAccessApi("Unable to access Pywhatkit api right now")
