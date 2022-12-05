# -*- coding: utf-8 -*-

import sublime
import sublime_plugin

import os
import subprocess


"""
Parquet package for Sublime Text, with python tooling.
https://github.com/yuj/sublime-parquet

Requires the python port of parquet-tools
https://github.com/ktrueda/parquet-tools
"""


COMMAND_NOT_FOUND_MSG = """'parquet-tools' not found.\n
Make sure python is in your PATH and install with 'pip install parquet-tools'
"""
PYTHON_COMMAND_LINE = "parquet-tools csv {0}"
UNICODE_ERROR = "Non-unicode characters prevented rendering: \n"


def run_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b"")


class ParquetCommand(sublime_plugin.TextCommand):
    def run(self, edit, filename=None):
        if filename is None or not filename.endswith(".parquet"):
            return
        command = PYTHON_COMMAND_LINE.format('"' + filename + '"')
        pos = 0
        try:
            for line in run_command(command):
                row = line.decode("utf-8")
                pos += self.view.insert(edit, pos, row.rstrip() + "\n")
        except (UnicodeDecodeError, TypeError):
            self.view.set_name(os.path.basename(filename))
            self.view.set_read_only(True)
            sublime.error_message(UNICODE_ERROR + str(line))
        except (FileNotFoundError, AttributeError):
            sublime.error_message(COMMAND_NOT_FOUND_MSG)
        self.view.set_name(os.path.basename(filename))
        self.view.set_read_only(True)


class OpenParquetFile(sublime_plugin.EventListener):
    def on_load(self, view):
        filename = view.file_name()
        if filename.endswith(".parquet"):
            sublime.status_message("opening parquet file: " + filename)
            parquet_view = view.window().new_file()
            view.close()
            parquet_view.run_command("parquet", {"filename": filename})
