from setuptools import setup

setup(
    name='eculib',
    version='1.0.19',
    description='A library for K-line based ECU communication',
    packages=['eculib'],
    entry_points={
        'console_scripts': ['eculib=eculib.__main__:Main'],
    },
    install_requires=['pylibftdi','pydispatcher'],
)
