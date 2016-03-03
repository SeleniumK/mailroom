# -*- utf-8 -*-

from setuptools import setup


setup(
    name="mailroom",
    description="Allows user to interact with donor information for charity.",
    version=0.1,
    author="Selena Flannery and Richard Tesmond",
    author_email="tesmonrd@gmail.com",
    license="MIT",
    py_modules=["mailroom"],
    package_dir={"": "mailroom"},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
