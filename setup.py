from setuptools import find_packages,setup
from typing import List


setup(
    name='Sensor',
    version='0.0.1',
    author="avanish",
    author_email="avanishdhake1@gmail.com",
    packages=find_packages(),
    install_requires=["pymongo"]
)