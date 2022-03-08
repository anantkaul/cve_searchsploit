#!/usr/bin/env python3

__author__ = "Anant Kaul"
__copyright__ = "Copyright 2022, Anant Kaul"
__license__ = "MIT"
__email__ = "anantkaul2000@gmail.com"

from setuptools import setup

setup(
    name='cve_searchsploit',
    version="1.6",
    license=__license__,
    description='Search an exploit in the local exploitdb database by its CVE',
    author=__author__,
    author_email=__email__,
    url='https://github.com/anantkaul/cve_searchsploit',
    download_url = 'https://github.com/anantkaul/cve_searchsploit/archive/master.tar.gz',
    package_dir={'cve_searchsploit': 'cve_searchsploit'},
    packages=['cve_searchsploit'],
    install_requires=[
        'requests',
        'progressbar2'
    ],
    entry_points={
        'console_scripts': ['cve_searchsploit = cve_searchsploit.main:main']
    },
    package_data={"cve_searchsploit": ["*.json"]}
)

