#!/usr/bin/env python3
"""
"""

import csv
import filecmp
import os
import re
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

    d = Path("/home/{}/skills/04-14".format(name))

    try:
        content = (d / "exp_cdf.py").read_text().strip()
        content = content.replace(" ", "")
        if "map(exp_cdf,xx)" in content:
            result["23-map-python"] = 1
    except:
        pass

    try:
        content = (d / "q1.csv").read_text().strip()
        content = re.sub(r"[^01]", "", content)
        if "00000100001000" in content:
            result["24-text-transform"] = 1
    except:
        pass

    try:
        content = (d / "q2.txt").read_text().strip()
        content = re.sub(r"[^a-z]", "", content)
        if "doeverythingstudentstellyou" in content:
            result["25-text-inverse-transform"] = 1
    except:
        pass


    return result


standards = """
    23-map-python
    24-text-transform
    25-text-inverse-transform
""".split()

if __name__ == "__main__":
    fields = ["name"] + standards 
    writer = csv.DictWriter(sys.stdout, fields)
    writer.writeheader()

    if 1 < len(sys.argv):
        name = sys.argv[1]
        result = score(name, standards)
        writer.writerow(result)
    else:
        names = os.listdir("/home")
        for name in names:
            result = score(name, standards)
            writer.writerow(result)
