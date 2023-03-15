# Small programs

 This repo stored some self-use small programs, please feel free to use it.  If you found any bugs, please report them at: [yyppiyt/small-programs/issues](https://github.com/yyppiyt/small-programs/issues) and I will try to fix them ASAP.

* [BulkRename](#bulkrename)
    * [Installation](#installation)
    * [Usage](#usage)
    * [Output template](#output-template)

## BulkRename

 BulkRename is a small python program that use to rename multiple files, the new filenames were stored in rename.csv.

 BulkRename supports Python 3.6 and above version.

### Installation

 Download the program from [yyppiyt/small-programs/BulkRename](https://github.com/yyppiyt/small-programs/tree/main/BulkRename)

### Usage

    python bulk-rename.py FOLDER CSV

### Output template

 Start the program with the folder path and csv path parameter
 
    python bulk-rename.py C:\Github\small-programs\BulkRename\sample D:\rename.csv

 The program will show the selected folder and csv file, then list all files that are waiting to be renamed and ask the user what to do next.

    Selected folder: C:\Github\small-programs\BulkRename\sample
    Selected csv: D:\rename.csv

    Files to be rename:
    "sample_01.txt" -> "sample_text_D01.txt"
    "sample_02.txt" -> "sample_text_D02.txt"
    "sample_03.txt" -> "sample_text_D03.txt"
    Confirm rename above files? (Y/N): 

 You can enter "list" to list all files again

    Confirm rename above files? (Y/N): list

    Files to be rename:
    "sample_01.txt" -> "sample_text_D01.txt"
    "sample_02.txt" -> "sample_text_D02.txt"
    "sample_03.txt" -> "sample_text_D03.txt"
    Confirm rename above files? (Y/N):

 Enter "update" to reload the csv file and the rename list

    Confirm rename above files? (Y/N): update
    Updating rename list...

    Files to be rename:
    "sample_01.txt" -> "sample_text_D01_ver2.txt"
    "sample_02.txt" -> "sample_text_D02_ver2.txt"
    "sample_03.txt" -> "sample_text_D03_ver2.txt"
    Confirm rename above files? (Y/N):

 Enter "Y" or "YES" to start renaming. After the operation, the numbers of successes and failures will be displayed on the last line.

    Confirm rename above files? (Y/N): y
    "sample_01.txt" renamed to "sample_text_D01_ver2.txt"
    "sample_02.txt" renamed to "sample_text_D02_ver2.txt"
    "sample_03.txt" renamed to "sample_text_D03_ver2.txt"
    Rename completed with 3 success and 0 fail

 Enter "N" or "NO" to abort the operation.

    Confirm rename above files? (Y/N): n
    Rename aborted, program ended

## KanColle
 Inoperative