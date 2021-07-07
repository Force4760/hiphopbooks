from setuptools import setup
setup(
    name='hhbooks',
    version='0.1.0',
    packages=['hhbooks'],
    install_requires=[
        "lyricsgenius",
        "colorthief"
    ],
    entry_points={
        'console_scripts': [
            'hhbooks = hhbooks.code.__main__:main'
        ]
    })
