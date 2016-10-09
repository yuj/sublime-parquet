# sublime-parquet
Reads Apache Parquet files in Sublime Text. The records are shown in JSON format, one JSON object per line. Parquet files are opened in read-only mode.

# Screenshot
![screenshot](https://raw.github.com/yuj/sublime-parquet/master/screenshot.png)

# Installation
Method 1: via Package Control

1. Make sure you have [Package Control](https://packagecontrol.io/installation) installed.
1. Open the Command Palette (`ctrl-shift-P` on Ubuntu; `command-shift-P` on macOS) and choose _Install Package_.
1. Choose _Parquet_ from the list.
(The package submission is underway.)

Method 2: manual

*macOS*
```shell
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
git clone https://github.com/yuj/sublime-parquet.git
```

*Ubuntu*
```shell
cd ~/.config/sublime-text-3/Packages
git clone https://github.com/yuj/sublime-parquet.git
```

# Requirement
This sublime package depends on the 'parquet-tools' software. Make sure it is installed and on your PATH. See [parquet-tools](https://github.com/Parquet/parquet-mr/tree/master/parquet-tools) for details.

On macOS, ```brew install parquet-tools``` .

On Ubuntu, see https://github.com/Parquet/parquet-mr/issues/321 to properly install the shell scripts.

