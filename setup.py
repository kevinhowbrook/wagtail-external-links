#!/usr/bin/env python
"""
Installs yourapp.
"""

from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="wagtail_external_links",
    version="1",
    description="External link formatting for templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevinhowbrook/wagtail-external-links",
    author="Kevin Howbrook",
    author_email="kbhowbrook@gmail.com",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=["wagtail>=2.4"],
)
