from setuptools import setup, find_packages

setup(
    name = 'nyc-crime-map',
    version = '0.2',
    description = 'Get data from the crime map',
    author = 'Thomas Levine',
    author_email = '_@thomaslevine.com',
    url = 'http://thomaslevine.com/!/nyc-crime-map/',
    entry_points = {'console_scripts': ['nyc-crime-map = nyc_crime_map:cli']},
    license = 'AGPL',
    packages = ['nyc_crime_map'],
    install_requires = [
        'requests>=2.3.0',
        'vlermv>=1.2.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.4',
    ],
)
