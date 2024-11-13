from setuptools import setup, find_packages

setup(
 name = 'mypackage',
 version = '1.0',
 packages = find_packages(exclude=['tests*']),
 instructions = open('readME.md').read(),
 install_requires = ['numpy'],
 author = 'Dr.HAS0',
 author_email = 'hammedimeji@yahoo.com'
)