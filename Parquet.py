# -*- coding: utf-8 -*-

import sublime
import sublime_plugin

import os
import subprocess


"""
Parquet package for Sublime Text, with python tooling.
https://github.com/dogversioning/sublime-parquet-python
Forked from https://github.com/yuj/sublime-parquet

External dependency: parquet-tools (https://github.com/ktrueda/parquet-tools)
"""


COMMAND_NOT_FOUND_MSG = "'parquet-tools' not found. Make sure python is in your PATH and install with 'pip install parquet-tools\n"
COMMAND_LINE = "parquet-tools csv {0}"


def run_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b"")


class ParquetCommand(sublime_plugin.TextCommand):
    def run(self, edit, filename=None):
        if filename is None or not filename.endswith(".parquet"):
            return

        pos = 0
        command = COMMAND_LINE.format(filename).split()

        try:
            for line in run_command(command):
                pos += self.view.insert(edit, pos, line.rstrip().decode("utf-8") + "\n")
        except FileNotFoundError:
            pos += self.view.insert(edit, pos, COMMAND_NOT_FOUND_MSG)

        self.view.set_name(os.path.basename(filename))
        self.view.set_read_only(True)


class OpenParquetFile(sublime_plugin.EventListener):
    def on_load(self, view):
        filename = view.file_name()
        if filename.endswith(".parquet"):
            sublime.status_message("opening parquet file: " + filename)
            print("opening parquet file: " + filename)
            parquet_view = view.window().new_file()
            view.close()
            parquet_view.run_command("parquet", {"filename": filename})
