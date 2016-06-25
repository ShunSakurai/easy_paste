'''
cd dropbox/codes/easy_paste
py -3.4 setup.py py2exe

rmdir /s __pycache__
rmdir /s dist

Libraries used:
import tkinter
import tkinter.filedialog
import csv
import os
import subprocess
import sys
import doctest
'''
from distutils.core import setup
import py2exe

setup(
    console=[{
        'author': 'Shun Sakurai',
        'dest_base': 'Easy Paste',
        'script': 'easy_paste.py',
        'version': '1.4.6',
    }],
    options={'py2exe': {
        'bundle_files': 2,
        'compressed': True,
        'excludes': ['_bz2', '_frozen_importlib', '_hashlib', '_lzma', '_ssl', 'argparse', 'calendar', 'datetime', 'difflib', 'inspect', 'locale', 'optparse', 'pdb', 'pickle', 'pydoc', 'pyexpat', 'pyreadline', 'zipfile'],
    }}
)
