# sublime-parquet-python
Reads Apache Parquet files in Sublime Text, extracted as CSVs. See the original [sublime-parquet](https://github.com/yuj/sublime-parquet) for a java based version.

# Screenshot
![screencap](https://raw.github.com/dogversioning/sublime-parquet-python/main/screencap.png)

# Installation
**via Package Control**

1. Make sure you have [Package Control](https://packagecontrol.io/installation) installed.
1. Open the Command Palette (`command-shift-P` on macOS; `ctrl-shift-P` on Ubuntu/Windows) and choose _Install Package_.
1. Choose _ParquetPython_ from the list.

# Requirements
You'll need to have a python environment in your path, and then install [parquet-tools](https://github.com/ktrueda/parquet-tools) with `pip install parquet-tools`

# Known Issues
Currently, there's no handling for non-UTF-8 characters - if, for example, you're using pokemon data to test and verify, make sure to deal with characters like the sex indicators of the Nidorinos or you may run into encoding issues on import. Don't ask me how long it took me to figure this out.