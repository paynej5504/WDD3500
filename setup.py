#imports packages
from setuptools import setup, find_packages
requires = [
'flask',
'url_for'
]
setup(
name='flask_first_app', #name of the app
version='0.0', #app version
description='My first Python web app built with Flask', #description of app
author='<Your actual name here>', #author's name
author_email='<Your actual e-mail address here>',
keywords='web flask',
packages=find_packages(),
include_package_data=True,
install_requires=requires
)
