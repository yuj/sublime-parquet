# sublime-parquet
Reads Apache Parquet files in Sublime Text. The records are shown in JSON format, one JSON object per line. Parquet files are opened in read-only mode.

# Screenshot
![screenshot](https://raw.github.com/yuj/sublime-parquet/master/screenshot.png)

# Installation
**via Package Control**

1. Make sure you have [Package Control](https://packagecontrol.io/installation) installed.
1. Open the Command Palette (`command-shift-P` on macOS; `ctrl-shift-P` on Ubuntu) and choose _Install Package_.
1. Choose _Parquet_ from the list.

# Requirement
This sublime package depends on the [parquet-tools](https://github.com/apache/parquet-mr/tree/master/parquet-tools) software. Make sure it is installed and on your PATH.

On macOS (or Ubuntu), run ```brew install parquet-tools```.

To install brew, visit http://brew.sh.

