'''
cd dropbox/codes/easy_paste
py -3.4 setup.py py2exe
'''
from distutils.core import setup
import py2exe

setup(
      console=[{'script': 'easy_paste.py', 'version': '1.2.0', 'dest_base': 'Easy Paste'}],
      options={'py2exe': {'bundle_files': 2}},
      )
