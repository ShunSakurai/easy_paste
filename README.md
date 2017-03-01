# easy_paste
A tool for generating easy-to-paste tables for quotes and weighted words from the analysis exported from memoQ

![Concept](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_concept.png)

![task sheet concept](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_task_sheet_concept.png)

## Description
You don't have to manually add up the number of words for creating quotes anymore. This tool generates easy-to-paste tables for quotes from the analysis exported from memoQ.

You can also calculate the weighted words and the translation and proofreading time for the files. memoQ now [tells us the weighted words](https://www.memoq.com/memoq-build-june), but this tool is still useful in that it can calculated the weighted words for sliced files, and it can provide the estimated time.

This program is coded in Python with tkinter and is distributed in .exe format through [py2exe](http://www.py2exe.org/).

The icon was created with [アイコン ウィザード](http://freewareplace.web.fc2.com/) and the installer is created with [Inno Setup](http://www.jrsoftware.org/isdl.php).

Japanese README will also be available upon request.

## Installation
This tool is currently only available for Windows at [Releases](https://github.com/ShunSakurai/easy_paste/releases).

All you have to do for installation and upgrading is to download and run the installer.

If you have the Python environment installed, you can run the source code with `python easy_paste.py`, `python3 easy_paste.py`, or `import easy_paste` even on Mac and on any OS.

## Build
To convert the Python code to .exe file, and to create an installer, follow steps below.

Requirements and procedures for the .exe file:

- [py2exe](http://www.py2exe.org/)
- Python 3.4 (py2exe is not compatible with Python 3.5 as far as I know)
- Run `py -3.4 setup.py py2exe` on a Windows machine

Requirements and procedures for the installer:

- [Inno Setup](http://www.jrsoftware.org/isdl.php)
- Open setup_installer.iss with Inno Setup Compiler and click Build > Compile

## Usage

### memoQ analysis file types
Please select one of the following options when exporting the statistics from memoQ

From Documents tab > Statistics:
- CSV (Per-file, Trados-compatible)
- CSV (Per-file, all information)

![Format](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_format.png)

From Project home > Overview > Reports > Analysis:
- CSV file exported by clicking 'export'

![Format](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_format2.png)

### Generating a table for quote
- You can open the program by double-clicking Easy Paste.exe or its alias.
- Choose CSV files exported from memoQ's statistics in above mentioned format
- Click "Generate table for quote"
- CSV files starting with "to_paste" is generated in the same folder as the original CSV files

![UI](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_ui.png)

### Copying and pasting the table
- Open the exported CSV file
- You can easily copy and paste the table to your quote
- Paste with "Keep Text Only" option in order to avoid messing up the font and the format

### Options
- You can choose the unit from "Word" or "Character." "Character" is only supported in all information CSV files or CSV files exported from "Reports." See [memoQ analysis file types](https://github.com/ShunSakurai/easy_paste#memoq-analysis-file-types) for details
- You can choose 50-74% matches are included in whether "New" or "Fuzzy"
- You can choose the format from "New, Fuzzy, and 100% and Repetitions" or ""New, Fuzzy, 100%, and Repetitions""
- You can choose the heading from "New Words" or "Translation -  New Words." I will add an option to create your own heading formats

![Four heading formats](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_heading.png)

### Calculating weighted words
The basic procedure is the same as in 'Generating a table for quote'

- Click "Calculate weighted words"
- CSV files starting with "weighted_" is generated in the same folder as the original CSV files
- Open the exported CSV file
- You can change the check 100% matches options and the words per day options and the result updates accordingly
- Beware that the time and weighted words are not rounded. Round the values if necessary using Excel's commands, etc.
- You can choose the format from the following two formats

![task sheet](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_task_sheet.png)
![task sheet](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_task_sheet2.png)

## Answers to FAQ, and known issues and workarounds

### Equations are lost when re-saving the CSV
When you save the weighted words table after editing it in Excel or Open Office, the equations are lost and only values are saved. After that, you cannot change the words/day and 100% review:Yes/No. To prevent this, try saving the file as Excel or Open Office formats.

## Features to come
### Working on
- Make the "Open files" dialog more useful
- Create your own heading formats
- Save last used settings
- Create an empty table when no file is imported
- Add total row and columns
- * Resolve an issue where analysis for grouped multilingual files fails

### Maybe later
- Open the tables from inside the program
- Retain the order of the slices of a file

### Features not coming
- Support HTML format to count characters. It turned out some CSV formats include character counts
- Open multiple analysis CSV files at once. The equations will become too complex
- Append the results at the bottom instead of overwriting the existing file. The equations will become too complex

Please [let me know](https://app.asana.com/-/share?s=132674863519245-jpqOgsUH4HdnKpFhvDDKXHfGUw0ccrb27xIIYgXyXV0-29199191293549) if you need any of the features as soon as possible.

## History
Please go to [Releases](https://github.com/ShunSakurai/easy_paste/releases) for the detailed history.

"*" at the beginning means bug-fixing.

## Contribution
This is just a personal project and I do not really know what kind of contribution I may get. Any [feedback](https://app.asana.com/0/264050103803746/list) and contribution is welcome!

Dear colleague translators and PMs, please help me brush up my English on this page.

## License
### Usage
You can use it for free.
© 2016-2017 Shun Sakurai

Please note that this tool is not officially tested and approved by our company. I try my best to maintain the accuracy and the compatibility, but please agree to use it 'at your own risk.'

###MIT License
The code is protected under MIT License. Please see license.txt for details.
