# sublime-parquet
Reads Apache Parquet files in Sublime Text. Can use several mechanisms for decoding - seee requirements.

# Screenshot
![screencap](https://raw.github.com/dogversioning/sublime-parquet-python/main/screencap.png)

# Installation
**via Package Control**

1. Make sure you have [Package Control](https://packagecontrol.io/installation) installed.
1. Open the Command Palette (`command-shift-P` on macOS; `ctrl-shift-P` on Ubuntu/Windows) and choose _Install Package_.
1. Choose _ParquetPython_ from the list.

# Requirements

## Python
You'll need to have a python environment in your path, and then install [parquet-tools](https://github.com/ktrueda/parquet-tools) with `pip install parquet-tools`.

## Java
You'll need to install version 1.12.0 of the [apache parquet-tools](https://github.com/apache/parquet-mr/releases/tag/apache-parquet-1.12.0). You can then toggle this in the package settings.

This is now deprecated - installing the python version is recommended. 
