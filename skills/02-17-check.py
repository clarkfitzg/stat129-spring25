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

#from IPython.core.debugger import set_trace


def score(name, standards):
    """score standards based on first name
    """
    result = {s: 0 for s in standards}
    result["name"] = name

    d = Path("/home/{}/skills/02-17".format(name))

    try:
        content = (d / "q1.csv").read_text()
        clean = content.split()
        #set_trace()
        if clean[0] == "53941":
            result["10-line-count"] = 1
    except:
        pass

    expected = subprocess.run(['head', '/stat129/diamonds.csv'],
                              capture_output=True, text=True).stdout
    try:
        content = (d / "q2.csv").read_text()
        if expected == content:
            result["11-head-large-file"] = 1
    except:
        pass

    expected = subprocess.run(['cut', '-d,', '-f7', '/stat129/diamonds.csv'],
                              capture_output=True, text=True).stdout
    try:
        content = (d / "q3.csv").read_text()
        if expected == content:
            result["12-cut-tabular-columns"] = 1
    except:
        pass

    expected = subprocess.run(['grep', 'Ideal', '/stat129/diamonds.csv'],
                              capture_output=True, text=True).stdout
    try:
        content = (d / "q4.csv").read_text()
        if expected == content:
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


if __name__ == "__main__":
    if 1 < len(sys.argv):
        name = sys.argv[1]
        result = score(name, standards)
        writer.writerow(result)
    else:
        for name in names:
            result = score(name, standards)
            writer.writerow(result)
