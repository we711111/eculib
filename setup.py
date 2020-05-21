from setuptools import setup

setup(
    name='eculib',
    version='1.0.37',
    description='A library for K-line based ECU communication',
    url='https://github.com/we711111/eculib',
    author='Sabsteef',
    author_email='',
    license='GPL-3',
    packages=['eculib'],
    entry_points={
        'console_scripts': ['eculib=eculib.__main__:Main'],
    },
    install_requires=['pylibftdi','pydispatcher'],
)
