from setuptools import setup

setup(
    name = 'notes',
    version = '0.1.0',
    packages = ['notes'],
    install_requires=[ 'plumbum', ],
    entry_points = {
        'console_scripts': [
            'notes = notes.__main__:Notes',
        ]
    })