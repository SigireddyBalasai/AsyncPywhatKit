from distutils.core import setup
import pathlib


def readme() -> str:
    with open(r"README.md") as f:
        README = f.read()
    return README


def reqs():
    with open("C:\\Users\\sigir\\PycharmProjects\\AsyncPywhatKit\\requirements.txt", "r") as f:
        requirements = [line.strip() for line in f]
        return requirements


setup(
    name="AsyncPywhatKit",
    packages=['AsyncPywhatKit.src', 'AsyncPywhatKit.src.Core'],
    version="2.1.1",
    license="MIT",
    description="AsyncPywhatKit is a Simple and Powerful WhatsApp Automation Library with many useful Features",
    author="SigireddyBalasai",
    author_email="sigireddybalasai@gmail.com",
    url="https://github.com/SigireddyBalasai/AsyncPywhatKit",
    download_url="https://github.com/SigireddyBalasai/AsyncPywhatKit/archive/refs/tags/1.0.tar.gz",
    keywords=["sendwhatmsg", "info", "playonyt", "search", "watch_tutorial", "async pywhatkit"],
    install_requires=reqs(),
    package_data={"pywhatkit": ["py.typed"]},
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
