#!/usr/bin/env python3
"""
First create dummy files: $ touch {alpha,bravo,charlie}{01..99}.{csv,txt}
"""

import csv
import filecmp
import os
import sys

from glob import glob
from pathlib import Path


def score(name, standards):
    """score standards based on first name
    """
    result = {s: 0 for s in standards}
    result["name"] = name

    d = Path("/home/{}/skills/02-10".format(name))

    try:
        content = (d / "q1.txt").read_text()
        clean = content.strip()
        if clean == "/home":
            result["06-navigate-directory"] = 1
    except:
        pass

    expected = "use SEP instead of non-blank to blank transition"
    try:
        content = (d / "q2.txt").read_text()
        if expected in content and len(content) < 100:
            result["07-read-man-page"] = 1
            result["08-copy-paste"] = 1
    except:
        pass

    expected = glob("/stat129/names/bravo*.txt")
    expected = {Path(p).name for p in expected}
    try:
        files = set(os.listdir(d))
        files.discard("q1.txt")
        files.discard("q2.txt")
        if files == expected:
            result["09-wildcards"] = 1
    except:
        pass

    return result


standards = """
06-navigate-directory
07-read-man-page
08-copy-paste
09-wildcards
""".split()

names = os.listdir("/home")
fields = ["name"] + standards 
writer = csv.DictWriter(sys.stdout, fields)
writer.writeheader()

for name in names:
    result = score(name, standards)
    writer.writerow(result)
