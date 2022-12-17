# sublime-parquet
Reads Apache Parquet files in Sublime Text using they python parquet-tools package. Files are rendered as CSVs.

# Screenshot
![screencap](https://raw.github.com/dogversioning/sublime-parquet-python/main/screencap.png)

# Installation
**via Package Control**

1. Make sure you have [Package Control](https://packagecontrol.io/installation) installed.
1. Open the Command Palette (`command-shift-P` on macOS; `ctrl-shift-P` on Ubuntu/Windows) and choose _Install Package_.
1. Choose _Parquet_ from the list.

# Requirements

 - Install [parquet-tools](https://github.com/ktrueda/parquet-tools) with `pip install parquet-tools`.
 - On Windows: make sure your python environment is in your path
 - On Mac/Linux: create a symlink from your python bin folder to the parquet-tools binary someplace on the system path, like `/usr/local/bin`
