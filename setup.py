'''
cd dropbox/codes/easy_paste
py -3.4 setup.py py2exe

Libraries used:
import tkinter
import tkinter.filedialog
import csv
import os
import subprocess
import sys
import doctest
'''
import os
import shutil

if os.path.exists('dist'):
    shutil.rmtree('dist')

from distutils.core import setup
import py2exe


dict_console = {
    'author': 'Shun Sakurai',
    'dest_base': 'Easy Paste',
    'icon_resources': [(1, './icons/easy_paste_icon.ico')],
    'script': 'easy_paste.py',
    'version': '1.5.8',
}
dict_options = {
    'bundle_files': 2,
    'compressed': True,
    'excludes': [
        '_bz2', '_frozen_importlib', '_hashlib', '_lzma', '_ssl',
        'argparse', 'calendar', 'datetime', 'difflib', 'inspect',
        'locale', 'optparse', 'pdb', 'pickle', 'pydoc', 'pyexpat',
        'pyreadline', 'zipfile'],
}


setup(
    console=[dict_console],
    options={'py2exe': {dict_options}}
)

shutil.rmtree('__pycache__')
print('.exe file v' + dict_console['version'], 'created.')
