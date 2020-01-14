
from setuptools import setup
import re

filepath = 'pdfshrink/__init__.py'
__version__ = re.findall(r'__version__ = \'(.*)\'', open(filepath).read())[0]

setup(
    name = 'pdfshrink',
    version = __version__,
    license = 'MIT',
    author = 'Tom de Geus',
    author_email = 'tom@geus.me',
    description = 'Script of shrink PDF files (wrapper around GhostScript)',
    long_description = 'Script of shrink PDF files (wrapper around GhostScript)',
    keywords = 'PDF, GhostScript',
    url = 'https://github.com/tdegeus/pdfshrink',
    packages = ['pdfshrink'],
    install_requires = ['docopt>=0.6.2', 'click>=4.0'],
    entry_points = {
        'console_scripts': ['pdfshrink = pdfshrink:main']})
