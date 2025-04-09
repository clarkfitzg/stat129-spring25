#!/usr/bin/env python3
"""
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

    d = Path("/home/{}/skills/04-07".format(name))

    try:
        f = d / "q1.out"
        if filecmp.cmp(f, "/stat129/class/skills/scratch/cityNm.txt"):
            result["22-xpath"] = 1
    except:
        pass

    try:
        f = d / "q1.txt"
        if filecmp.cmp(f, "/stat129/class/skills/scratch/cityNm.txt"):
            result["22-xpath"] = 1
    except:
        pass

    try:
        content = (d / "log.py").read_text().strip()
        content = content.replace(" ", "")
        #y = [log(x) for x in range(1, 11)]
        if "map(log,range(1,11))" in content:
            result["23-map-python"] = 1
    except:
        pass

    return result


standards = """
    22-xpath
    23-map-python
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
