from enum import Enum
import asyncio
import aiohttp


class ConnectionType(Enum):
    GOOGLE = "https://www.google.com"
    DNS = "https://1.1.1.1"

async def check_connection_type(url: str) -> bool:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return response.status == 200
    except aiohttp.ClientError:
        return False

async def check_connection() -> bool:
    """
    Check the Internet connection of the Host Machine.

    Returns:
        bool: True if the Host Machine is connected to the Internet, False otherwise.
    """
    google_connection = await check_connection_type(ConnectionType.GOOGLE.value)
    dns_connection = await check_connection_type(ConnectionType.DNS.value)
    return google_connection and dns_connection
