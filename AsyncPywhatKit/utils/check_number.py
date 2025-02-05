from pydantic import BaseModel, validator

"""
This module contains utility functions for checking phone numbers.
"""

class PhoneNumber(BaseModel):
    """
    A class to represent a phone number.
    """
    number: str

    @validator('number')
    def validate_number(cls, v: str) -> str:
        """
        Validate the phone number.

        Args:
            v (str): The phone number to validate.

        Returns:
            str: The validated phone number.

        Raises:
            ValueError: If the phone number is invalid.
        """
        if not ("+" in v or "_" in v):
            raise ValueError('Invalid phone number')
        return v

async def check_number(number: str) -> bool:
    """
    Checks if the given phone number is valid or not.

    A valid phone number is defined as one that contains either a '+' or an '_'.

    Args:
        number (str): The phone number to check.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    try:
        PhoneNumber(number=number)
        return True
    except ValueError:
        return False