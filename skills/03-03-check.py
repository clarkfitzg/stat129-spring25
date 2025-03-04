#!/usr/bin/env python3
"""
    parallel --dry-run bash /stat129/class/bash-script-examples/script2.sh ::: /stat129/17*.csv.gz > /stat129/class/skills/scratch/03-03-q3.out
"""

import csv
import filecmp
import os
import subprocess
import sys

from glob import glob
from pathlib import Path

from IPython.core.debugger import set_trace


def score(name, standards):
    """score standards based on first name
    """
    result = {s: 0 for s in standards}
    result["name"] = name

    d = Path("/home/{}/skills/03-03".format(name))

    #set_trace()
    try:
        content = (d / "q1.txt").read_text().strip()
        if content == "549.5":
            result["18-run-python-script"] = 1
    except:
        pass

    try:
        f = (d / "GlobalSummaryTimeSeries-2021.pdf")
        expected = "/stat129/class/skills/scratch/GlobalSummaryTimeSeries-2021.pdf"
        if filecmp.cmp(f, expected):
            result["16-transfer-files"] = 1
    except:
        pass

    try:
        f = (d / "q3.txt")
        expected = "/stat129/class/skills/scratch/03-03-q3.out"
        if filecmp.cmp(f, expected):
            result["17-parallelize"] = 1
    except:
        pass

    return result


standards = """
    16-transfer-files
    17-parallelize
    18-run-python-script
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
