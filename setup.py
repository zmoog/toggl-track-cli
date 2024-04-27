from setuptools import setup
import os

VERSION = "0.5.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="toggl-track",
    description="CLI tool and Python library to access Toggl Track https://toggl.com/track/",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Maurizio Branca",
    url="https://github.com/zmoog/toggl-track",
    project_urls={
        "Issues": "https://github.com/zmoog/toggl-track/issues",
        "CI": "https://github.com/zmoog/toggl-track/actions",
        "Changelog": "https://github.com/zmoog/toggl-track/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["toggl_track"],
    entry_points="""
        [console_scripts]
        tgl=toggl_track.cli:cli
    """,
    install_requires=[
        "click == 8.1.7",
        "pydantic < 2",
        "requests == 2.31.0",
        "rich == 13.7.1",
        ],
    extras_require={
        "test": [
            "pytest == 7.4.4",
            "pytest-recording == 0.13.1",
            ]
    },
    python_requires=">=3.7",
)
