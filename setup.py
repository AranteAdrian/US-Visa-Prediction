from setuptools import setup, find_packages
"""
This is the setup script for the US Visa Prediction project.
This script uses setuptools to package the project. It specifies the project
name, version, author's email, and the packages to include.
Attributes:
    name (str): The name of the project.
    version (str): The current version of the project.
    email (str): The email address of the author.
    packages (list): A list of all Python import packages that should be included in the distribution package.

Relation to requirements.txt:
    The `-e .` entry in the `requirements.txt` file indicates that the current project directory should be installed
    in "editable" mode. This means that any changes made to the project code will be immediately reflected without
    needing to reinstall the package. The `setup.py` script is used by `pip` to install the project in this mode,
    allowing for easy development and testing of the project.
"""

setup (
    name='us_visa',
    version='0.0.0',
    email='aranteadriandominique3@gmail.com',
    packages=find_packages(),
)