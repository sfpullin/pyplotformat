from setuptools import setup, find_packages
import os
import codecs


with open("README.md") as file:
    long_description = file.read()

REQUIREMENTS = ['matplotlib', 'pypdf']

CLASSIFIERS = [
'Programming Language :: Python :: 3.9'
'Programming Language :: Python :: 3.10',
]


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(name='pyplotformat',
version=get_version("pyplotformat/__init__.py"),
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