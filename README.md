![image](https://media.discordapp.net/attachments/842794167134453820/882227960613048350/unknown.png?width=1440&height=420)

[![image](https://flat.badgen.net/github/stars/SigireddyBalasai/AsyncPywhatKit)](https://github.com/Ankit404butfound/AsyncPywhatKit/stargazers)
[![image](https://flat.badgen.net/github/forks/SigireddyBalasai/AsyncPywhatKit)](https://github.com/Ankit404butfound/AsyncPywhatKit/network/members)
[![image](https://flat.badgen.net/github/open-issues/SigireddyBalasai/AsyncPywhatKit)](https://github.com/SigireddyBalasai/AsyncPywhatKit/issues)
[![image](https://flat.badgen.net/github/open-prs/SigireddyBalasai/AsyncPywhatKit)](https://github.com/SigireddyBalasai/AsyncPywhatKit/pulls)
[![image](https://flat.badgen.net/github/commits/SigireddyBalasai/AsyncPywhatKit)](https://github.com/SigireddyBalasai/AsyncPywhatKit/commits/master)
[![image](https://flat.badgen.net/github/license/SigireddyBalasai/AsyncPywhatKit)](https://github.com/SigireddyBalasai/AsyncPywhatKit/LICENCE)
[![image](https://flat.badgen.net/github/contributors/SigireddyBalasai/AsyncPywhatKit)](https://github.com/SigireddyBalasai/AsyncPywhatKit/graphs/contributors)
[![image](https://flat.badgen.net/github/release/SigireddyBalasai/AsyncPywhatKit)](https://github.com/SigireddyBalasai/AsyncPywhatKit/releases)
![image](https://img.shields.io/github/languages/count/SigireddyBalasai/AsyncPywhatKit)
![image](https://img.shields.io/github/languages/top/SigireddyBalasai/AsyncPywhatKit)
![image](https://img.shields.io/librariesio/release/pypi/AsyncPywhatKit)
![image](https://img.shields.io/github/repo-size/SigireddyBalasai/AsyncPywhatKit)
<a href="https://scan.coverity.com/projects/sigireddybalasai-asyncpywhatkit">
  <img alt="Coverity Scan Build Status"
       src="https://img.shields.io/coverity/scan/27211.svg"/>
</a>
<!-- ![logo](https://github.com/Ankit404butfound/PyWhatKit/raw/master/Images/logo.png?raw=true) -->


[AsyncPywhatKit](https://pypi.org/project/AsyncPywhatKit/) is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup. Currently, it is one of the most popular library for WhatsApp and YouTube automation. New updates are released frequently with new features and bug fixes.

# Links

- **Join our discord server - https://discord.gg/NDXdB6tNwa**
- **Documentation - [Wiki](https://github.com/SigireddyBalasai/AsyncPywhatKit/wiki/)**

## Installation and Supported Versions

AsyncPywhatKit is available on PyPi:

```bash
python3 -m pip install AsyncPywhatKit
```

```bash
pip3 install AsyncPywhatKit
```

PyWhatKit officially supports Python 3.8+.

## Cloning the Repository

```bash
git clone https://github.com/SigireddyBalasai/AsyncPywhatKit
```
```py
import asyncio
import AsyncPywhatKit


async def main():
    # Send a WhatsApp Message to a Contact at 1:30 PM
    await AsyncPywhatKit.sendwhatmsg("+910123456789", "Hi", 13, 30)

    # Same as above but Closes the Tab in 2 Seconds after Sending the Message
    await AsyncPywhatKit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

    # Send an Image to a Group with the Caption as Hello
    await AsyncPywhatKit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

    # Send an Image to a Contact with the no Caption
    await AsyncPywhatKit.sendwhats_image("+910123456789", "Images/Hello.png")

    # Send a WhatsApp Message to a Group at 12:00 AM
    await AsyncPywhatKit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

    # Send a WhatsApp Message to a Group instantly
    await AsyncPywhatKit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

    # Play a Video on YouTube
    await AsyncPywhatKit.playonyt("PyWhatKit")


asyncio.run(main())
```

For more Examples and Functions, have a look at the [Wiki](https://github.com/SigireddyBalasai/AsyncPywhatKit/wiki/).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Be sure to read the [Guidelines](https://github.com/SigireddyBalasai/AsyncPywhatKit/blob/main/CONTRIBUTING.md) before Contributing.

## License

Apache license 2.0
For more information see [this](https://github.com/SigireddyBalasai/AsyncPywhatKit/blob/main/LICENSE)
