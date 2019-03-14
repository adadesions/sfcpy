"""Setup script for sfcpy"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="sfcpy",
    version="1.1.0",
    description="Space-Filling Curve library for image-processing tasks",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/adadesions/sfcpy",
    author="adadesions",
    author_email="adadesions@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["sfcpy"],
    include_package_data=True,
    install_requires=[
        "numpy", "matplotlib", "PIL"
    ],
    entry_points={"console_scripts": ["sfcpy=sfcpy.__main__:main"]},
)