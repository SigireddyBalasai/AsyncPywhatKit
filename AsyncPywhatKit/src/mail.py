import re
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from typing import Union

from .Core.exceptions import UnsupportedEmailProvider


async def send_mail(
    email_sender: str,
    password: str,
    subject: str,
    message: Union[str, MIMEText],
    email_receiver: str,
) -> None:
    """Send an Email"""
    domain = re.search("(?<=@)[^.]+(?=\\.)", email_sender)

    hostnames = {
        "gmail": "smtp.gmail.com",
        "yahoo": "smtp.mail.yahoo.com",
        "outlook": "smtp.live.com",
        "aol": "smtp.aol.com",
    }

    hostname = None
    for x in hostnames:
        if x == domain.group():
            hostname = hostnames[x]
            break

    if hostname is None:
        raise UnsupportedEmailProvider(f"{domain.group()} is not Supported Currently!")

    with smtplib.SMTP_SSL(hostname, 465) as smtp:
        smtp.login(email_sender, password)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = email_sender
        msg["To"] = email_receiver
        msg.set_content(message)

        smtp.send_message(msg)
        print("Email Sent Successfully!")


async def send_hmail(
    email_sender: str, password: str, subject: str, html_code: str, email_receiver: str
) -> None:
    """Send an Email with HTML Code"""
    message = MIMEText(html_code, "html")
    await send_mail(email_sender, password, subject, message, email_receiver)
