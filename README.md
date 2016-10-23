# easy_paste
A tool for generating easy-to-paste tables for quotes and weighted words from the analysis exported from memoQ

![Concept](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_concept.png)

![task sheet concept](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_task_sheet_concept.png)

## Description
You don't have to manually add up the number of words for creating quotes anymore. This tool generates easy-to-paste tables for quotes from the analysis exported from memoQ.

You can also calculate the weighted words and the translation and proofreading time for the files. memoQ now [tells us the weighted words](https://www.memoq.com/memoq-build-june), but this tool is still useful in that it provides the estimated time.

This program is coded in Python with tkinter and is distributed in .exe format through [py2exe](http://www.py2exe.org/).

The icon was created with [アイコン ウィザード](http://freewareplace.web.fc2.com/) and the installer is created with [Inno Setup](http://www.jrsoftware.org/isdl.php).

Japanese README will also be available upon request.

## Installation
This tool is currently only available for Windows at [Releases](https://github.com/ShunSakurai/easy_paste/releases).

All you have to do for installation and upgrading is to download and run the installer.

This program needs to be **kept in the folder** to work. It does not work by itself.

If you have the Python environment installed, you can run the source code with `python(3) easy_paste.py` or `import easy_paste` even on Mac and on any OS.

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

### Generating a table
- You can open the program by double-clicking Easy Paste.exe or its alias.
- Choose a CSV file exported from memoQ's statistics in above mentioned format
- Click "Generate table for quote!"
- A CSV file starting with "to_paste" is generated in the same folder as the original CSV file

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
The basic procedure is the same as in 'Generating a table'

- Click "weighted words!"
- A CSV file starting with "weighted_" is generated in the same folder as the original CSV file
- Open the exported CSV file
- You can change the words per day and the result updates accordingly
- Beware that the time and weighted words are not rounded. Round the values if necessary using Excel's commands, etc.
- You can choose the format from the following two formats

![task sheet](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_task_sheet.png)
![task sheet](https://raw.github.com/wiki/ShunSakurai/easy_paste/easy_paste_task_sheet2.png)

## Features to come
### Working on
- Make the code more [readable](http://www.amazon.com/dp/0596802293)
- Make the "Open files" dialog more useful
- Create your own heading formats

### Maybe later
- Save last used settings
- Open the CSV files from inside the program

### Features not coming
- Support HTML format to count characters. It turned out some CSV formats include character counts
- Open multiple analysis CSV files at once. The equations will become too complex
- Append the results at the bottom instead of overwriting the existing file. The equations will become too complex

Please [let me know](https://app.asana.com/-/share?s=132674863519245-jpqOgsUH4HdnKpFhvDDKXHfGUw0ccrb27xIIYgXyXV0-29199191293549) if you need any of the features as soon as possible.

## History
"*" at the beginning means bug-fixing.
For detailed history, please go to [Releases](https://github.com/ShunSakurai/easy_paste/releases).

### v1.6.2, October 23, 2016
- Avoid using comma in the exported CSV file
- * Correct the position of the entry field

### v1.6.0, September 27, 2016
- Check for and download updates online
- Support X-translated segments
- Make usability improvements
- * Correct incorrect equations in weighted words in the second format

### v1.5.10, August 16, 2016
- Ask 50-74% matches are whether new or fuzzy
- Semiautomate the set-up process with shutil module

### v1.5.8, July 27, 2016
- Add disclaimer

### v1.5.7, July 19, 2016
- Make the path in the entry field the initial path when choosing the file

### v1.5.6, July 5, 2016
- * Resolve an issue where file names without language code cause an error

### v1.5.5, July 5, 2016
- Display the options for quotes in the results
- Support characters as the unit
- Move the summed up word counts on top of the results

### v1.5.2, July 4, 2016
- Create the installer
- Create the icon

### v1.5.0, July 2, 2016
- Sum up the word counts of the same language

### v1.4.11, July 1, 2016
- * Resolve an issue where decoding UTF-8 text with BOM fails

### v1.4.10, June 29, 2016
- Support two weighted words and time formats
- Keep the entry fields uncleared when open file dialog is canceled
- Support other memoQ analysis formats

### v1.4.7, June 25, 2016
- Change the weighted word and time format
- Open the folder from inside the program on non-Windows platform
- Make the weighted words compatible with non-Excel programs

### v1.4.4, June 15, 2016
- * Handle file names without a period '.'
- Make small improvements

### v1.4.3, June 15, 2016
- Open the folder from inside the program
- Make the code slightly less messy

### v1.4.1, June 14, 2016
- * Correct the wrong equations

### v1.4.0, June 14, 2016
- Calculate the weighted words and translation and proofreading time

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

Please note that this tool is not officially tested and approved by our company. I try my best to maintain the accuracy and the compatibility, but please agree to use it 'at your own risk.'

© 2016 Shun Sakurai
