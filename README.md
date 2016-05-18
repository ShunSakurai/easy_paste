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

### Generating a table

- You can open the program by double-clicking Easy Paste.exe or its alias.
- Choose a Trados-compatible CSV file exported from memoQ's statistics
- Click "Generate table!"
- A CSV file starting with "to_paste" is generated in the same folder as the original CSV file

![UI](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_ui.png)

### Copying and pasting the table

- Open the exported CSV file
- You can easily copy and paste the table to your quote
- Paste with "Keep Text Only" option in order to avoid messing up the font and the format

### Options

- You can choose the format from "New, Fuzzy, and 100% and Repetitions" or ""New, Fuzzy, 100%, and Repetitions""
- You can choose the heading from "New Words" or "Translation -  New Words." I will add an option to create your own heading formats

![Four heading formats](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_heading.png)

### memoQ analysis file types
Please select the following option when exporting the statistics from memoQ

- CSV (Per-file, Trados-compatible)

![Format](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_format.png)

## Known issues and workarounds

### Garbled UTF-8 CSV files opened with Shift-JIS Excel
If you simply open a CSV file encoded with UTF-8 with Microsoft Excel in an environment whose default encoding is Shift-JIS or any other non-Unicode encoding, the characters are likely to be garbled. There are many remedies to this, but the simplest solutions are as follows:

- Change the extension from .csv to .txt. A dialog window pops up and allows you to select the encoding
- Open the CSV files with Notepad. Rows are displayed merely as lines and the items are not separated, but at least they are displayed correctly
- Download CSV openers like [OpenOffice](https://www.openoffice.org/product/calc.html) Calc

## Features to come
### Working on
- Make the code more [readable](http://www.amazon.com/dp/0596802293)
- Prepare the installer
- Prepare the icon
- Make the "Open files" dialog more useful
- Calculate the weighted words
- Preview the task sheet (calculated words and time table)
- Create your own heading formats

### Maybe later
- Save last used settings

### Features not coming
- Support HTML format to count characters. It turned out we can use word counts for Asian characters

Please [let me know](https://app.asana.com/-/share?s=132674863519245-jpqOgsUH4HdnKpFhvDDKXHfGUw0ccrb27xIIYgXyXV0-29199191293549) if you need any of the features as soon as possible.

## History
"*" at the beginning means bug-fixing.
For detailed history, please go to [Releases](https://github.com/ShunSakurai/easy_paste/releases).

### v1.3.2, May 18, 2016
- Simplify the tool by deleting the option for characters or HTML files

### v1.3.1, May 16, 2016
- Move with the Tab key and select with the Enter key

### v1.3.0, May 15, 2016
- Display 101% (Repetition) and 100% joined or separately
- Add contact information
- Support multilingual projects
- Add several heading formats such as "Translation - New Words"
- Change the button name from Run to Generate table

### v1.2.3, April 24, 2016
- Add some spaces above and below buttons
- Reduce the size of the dist folder

### v1.2.1, April 22, 2016
- * Include Context TM in Repetitions and 100% Matches
- Add to GitHub
- Support both semicolon and tab delimiters
- Open the csv file and detect the delimiter

## Contribution
This is just a personal project and I do not really know what kind of contribution I may get. Any [feedback](https://app.asana.com/-/share?s=132674863519245-jpqOgsUH4HdnKpFhvDDKXHfGUw0ccrb27xIIYgXyXV0-29199191293549) and contribution is welcome!

Dear colleague translators and PMs, please help me brush up my English on this page.

## License
You can use it for free.

© 2016 Shun Sakurai
