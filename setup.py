from setuptools import setup, find_packages

with open("README.md") as file:
    long_description = file.read()

REQUIREMENTS = ['matplotlib', 'pypdf']

CLASSIFIERS = [
'Programming Language :: Python :: 3.9'
'Programming Language :: Python :: 3.10',
]


setup(name='pyplotformat',
version="0.0.4",
description='Tool for fast and consistent plot generation with the Matplotlib library.',
long_description=long_description,
url='https://github.com/sfpullin/plotter',
author='Shaun Pullin',
author_email='sp16189@bristol.ac.uk',
license='MIT',
classifiers=CLASSIFIERS,
install_requires=REQUIREMENTS,
packages=find_packages(exclude=['tests']),
include_package_data=True,
keywords=''
)