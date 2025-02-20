#!/usr/bin/env python3
"""
First download diamonds.csv
"""

import csv
import filecmp
import os
import subprocess
import sys

from glob import glob
from pathlib import Path


def score(name, standards):
    """score standards based on first name
    """
    result = {s: 0 for s in standards}
    result["name"] = name

    d = Path("/home/{}/skills/02-17".format(name))

    try:
        content = (d / "q1.txt").read_text()
        clean = content.split()
        if clean[0] == "53941":
            result["10-line-count"] = 1
    except:
        pass

    expected = subprocess.run(['head', '/stat129/diamonds.csv'],
                              capture_output=True, text=True).stdout
    try:
        content = (d / "q2.txt").read_text()
        if expected == content
            result["11-head-large-file"] = 1
    except:
        pass

    expected = subprocess.run(['cut', '-d,', '-f7', '/stat129/diamonds.csv'],
                              capture_output=True, text=True).stdout
    try:
        content = (d / "q3.txt").read_text()
        if expected == content
            result["12-cut-tabular-columns"] = 1
    except:
        pass

    expected = subprocess.run(['grep', 'Ideal', '/stat129/diamonds.csv'],
                              capture_output=True, text=True).stdout
    try:
        content = (d / "q4.txt").read_text()
        if expected == content
            result["13-grep-lines"] = 1
    except:
        pass

    return result


standards = """
10-line-count
11-head-large-file
12-cut-tabular-columns
13-grep-lines
""".split()

names = os.listdir("/home")
fields = ["name"] + standards 
writer = csv.DictWriter(sys.stdout, fields)
writer.writeheader()

for name in names:
    result = score(name, standards)
    writer.writerow(result)
