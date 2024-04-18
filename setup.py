"""Python setup.py for auth_test package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("auth_test", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="auth_test",
    version=read("auth_test", "VERSION"),
    description="Awesome auth_test created by vitorecomp",
    url="https://github.com/vitorecomp/auth-test/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="vitorecomp",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["auth_test = auth_test.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
