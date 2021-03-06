# Easy Paste
A tool for generating easy-to-paste tables for quotes and weighted words from the analysis exported from memoQ

This project is discontinued and will not be updated.

![Concept](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_concept.png)

![task sheet concept](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_task_sheet_concept.png)

## Description
You don't have to manually add up the number of words for creating quotes anymore. This tool generates easy-to-paste tables for quotes from the analysis exported from memoQ.

You can also calculate the weighted words and the translation and proofreading time for the files. memoQ now [tells us the weighted words](https://www.memoq.com/memoq-build-june), but this tool is still useful in that it can calculate the weighted words for sliced files, and it can provide the estimated time.

This program is coded in Python with tkinter and is distributed in .exe format through [PyInstaller](http://www.pyinstaller.org/) and [Verpatch](https://ddverpatch.codeplex.com/releases).

The icon was created with [アイコン ウィザード](http://freewareplace.web.fc2.com/) and the installer is created with [Inno Setup](http://www.jrsoftware.org/isdl.php).

Japanese README will also be available upon request.

## Installation
This tool is currently only available for Windows at [Releases](https://github.com/ShunSakurai/easy_paste/releases).

All you have to do for installation and upgrading is to download and run the installer.

If you have the Python environment installed, you can run the source code with `python easy_paste.py`, `python3 easy_paste.py`, or `import easy_paste` even on Mac and on any OS.

## Build
To convert the Python code to .exe file, and to create an installer, follow steps below.

### Requirements
- [Python 3](https://www.python.org/downloads/)
- [PyInstaller](http://www.pyinstaller.org/)
- [Verpatch](https://ddverpatch.codeplex.com/releases), add it to PATH
- [Inno Setup](http://www.jrsoftware.org/isdl.php)
- Minimum display resolution height: 900 pixels

### Procedures
- Run `py -B setup.py` on a Windows machine. `-B` is optional
- You may have to set alias to make py = python3

## Prerequisites
### Supported memoQ analysis file types
When exporting the statistics from memoQ, select one of the following options. Please note that Trados-compatible format doesn't contain character counts.

From Documents tab > Statistics:
- CSV (Per-file, all information)
- CSV (Per-file, Trados-compatible) * only support "word" counts

![Format](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_format.png)

From Project home > Overview > Reports > Analysis:
- CSV file exported by clicking 'export' is also supported

![Format](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_format2.png)

## Usage
### Common
- You can open the program by double-clicking Easy Paste.exe or its alias
- Choose CSV files exported from memoQ's statistics in above mentioned format
- After exporting the table, the exported CSV file is automatically opened
- You can move along the UI items with "Tab" key and invoke the focused item with the space bar

![UI](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_ui.png)

### Generating a table for quote
- Click "Generate table for quote"
- CSV files starting with "quote" is generated in the same folder as the original CSV files

#### Copying and pasting the table
- Open the exported CSV file
- You can easily copy and paste the table to your quote
- Paste with "Keep Text Only" option in order to avoid messing up the font and the format

#### Options
- You can choose the unit from "Word" or "Character." "Character" is only supported in all information CSV files or CSV files exported from "Reports." See [Supported memoQ analysis file types](https://github.com/ShunSakurai/easy_paste#supported-memoq-analysis-file-types) for details
- You can freely customize the match rate categories. By default, match rates are divided into "New, Fuzzy, and 100% and Repetitions"
- You can choose the heading from "New Words" or "Translation -  New Words"

![Four heading formats](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_heading.png)

### Calculating weighted words
The basic procedure is the same as in 'Generating a table for quote'

- Click "Calculate weighted words"
- CSV files starting with "weighted" is generated in the same folder as the original CSV files
- You can choose the format from the following two formats

#### Editing and saving the table
- Beware that the time and weighted words are not rounded. Round the values if necessary using Excel's commands, etc.
- Total and subtotal are automatically calculated and corresponding row and columns are added
- You can change the check 100% matches options and the words per day options and the result updates accordingly
- After editing, save the file in a file format other than CSV to retain the equations. See [Equations are lost when re-saving the CSV](https://github.com/ShunSakurai/easy_paste#equations-are-los- when-re-saving-the-CSV)

![task sheet](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_task_sheet.png)
![task sheet](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_task_sheet2.png)

## Answers to FAQ, and known issues and workarounds
### Equations are lost when re-saving the CSV
When you save the weighted words table after editing it in Excel or Open Office, the equations are lost and only values are saved. After that, you cannot change the words/day and 100% review:Yes/No. To prevent this, try saving the file as Excel or Open Office formats.

### 101% matches are ignored in weighted word table

## Features to come
### Working on
- Create your own heading formats
- \* Resolve an issue where analysis for grouped multilingual files fails

### Maybe later
- Save last used settings
- Enable the user to change result file name

### Features not coming
- Support HTML format to count characters. It turned out some CSV formats include character counts
- Append the results at the bottom instead of overwriting the existing file. The equations will become too complex

Please let me know from [Github Issues](https://github.com/ShunSakurai/easy_paste/issues) or [Asana](https://app.asana.com/0/264050103803746/list) if you need any of the features as soon as possible.

## History
Please go to [Releases](https://github.com/ShunSakurai/easy_paste/releases) for the detailed history.

"*" at the beginning means bug-fixing.

## Contribution
This is just a personal project and I do not really know what kind of contribution I may get. Any feedback and contribution from [Github Issues](https://github.com/ShunSakurai/easy_paste/issues) or [Asana](https://app.asana.com/0/264050103803746/list) is welcome!

Dear colleague translators and PMs, please help me brush up my English on this page.

## License
### Usage
You can use it for free.
© 2016-2018 Shun Sakurai

Please note that this tool is not officially tested and approved by our company. I try my best to maintain the accuracy and the compatibility, but please agree to use it 'at your own risk.'

### MIT License
The code is protected under MIT License. Please see license.txt for details.
