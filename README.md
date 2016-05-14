# easy_paste
A tool for generating easy-to-paste tables for quotes from the analysis exported from memoQ

[Japanese README](https://github.com/ShunSakurai/easy_paste/blob/master/README_jpn.md) will also be available.

![Concept](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_concept.png)

## Description
You don't have to manually add up the number of words for creating quotes anymore. This tool generates easy-to-paste tables for quotes from the analysis exported from memoQ.
This program is coded in Python with tkinter and is distributed in .exe format through [py2exe](http://www.py2exe.org/).

## Installation
This tool is currently only available for Windows at [Releases](https://github.com/ShunSakurai/easy_paste/releases).
Installer is now under development. In the meantime, please follow the steps below:

- Download dist.zip and decompress it
- Rename the folder to "easy_paste" or any name you like
- Move it to C:\Program Files
- Create a shortcut of the .exe file and add it to your Desktop, to your tools folder, or to C:\ProgramData\Microsoft\Windows\Start Menu\Programs

When you use an updated version, you only have to move the files and folders with newer dates.
This program needs to be **kept in the folder** to work. It does not work by itself.

If you have the Python environment installed, you can run the source code with `python(3) easy_paste.py` or `import easy_paste` even on Mac and on any OS.

## Usage

### Overview
You can open the program by double-clicking Easy Paste.exe or its alias.

- Choose a Trados-compatible CSV file or a html file exported from memoQ's statistics
- Currently only CSV files are supported
- Click "Run!"

- Open the exported CSV file
- You can easily copy and paste the table to your quote

![UI](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_ui.png)

### Options
You can choose the unit from "word" or "character". Currently only "word" is supported.

### memoQ analysis file types
Two file types will be supported:

- CSV (Per-file, Trados-compatible)
- HTML (Reflecting displayed results)
- Currently only a CSV file is supported

![Format](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_format.png)

## Features to come
### Working on
- Support HTML format to count characters
- Make the code more [readable](http://www.amazon.com/dp/0596802293)
- Prepare the installer
- Prepare the icon
- Make the "Open files" dialog more useful

### Maybe later
- Add the option to display 101%(Repetition) and 100% separately
- Save last used settings

Please let me know if you need any of the features as soon as possible.

## History
"*" at the beginning means bug-fixing.
For detailed history, please go to [Releases](https://github.com/ShunSakurai/easy_paste/releases).

### Newest version
- Add several label formats such as "Translation - New Words"

### v1.2.3, April 24, 2016
- Add some spaces above and below buttons
- Reduce the size of the dist folder

### v1.2.1, April 22, 2016
- * Include Context TM in Repetitions and 100% Matches
- Add to GitHub
- Support both semicolon and tab delimiters
- Open the csv file and detect the delimiter

## Contribution
This is just a personal project and I do not really know what kind of contribution I may get. Any feedback and contribution is welcome!

Dear colleague translators and PMs, please help me brush up my English on this page.

## License
You can use it for free.

© 2016 Shun Sakurai
