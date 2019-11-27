# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
import re

main_py = open('sharesync/__init__.py').read()
metadata = dict(re.findall("__([A-Z]+)__ = '([^']+)'", main_py))
__VERSION__ = metadata['VERSION']

setup(
    name='sharesync',
    version=__VERSION__,
    author='APSL · Bernardo Cabezas Serra',
    author_email='bcabezas@apsl.net',
    packages=find_packages(),
    license='GPL',
    description="Sharepoint migration tool based on rclone",
    long_description=open('README.rst').read(),
    entry_points={
        'console_scripts': [
            'sbackup = sharesync.main:main',
        ],
    },
    install_requires=[
        'click',
        'sh',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe=False,
)
