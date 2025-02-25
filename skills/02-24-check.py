#!/usr/bin/env python3
"""
    parallel --dry-run grep "needle" ::: /stat129/hay/stack* > scratch/02-24-4.out
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

    d = Path("/home/{}/skills/02-24".format(name))

    #set_trace()
    try:
        content = (d / "q1.txt").read_text()
        clean = set(content.split())
        wrong = set("od tr cut head >".split())
        wrong = clean.intersection(wrong)
        if "grep" in clean and not wrong:
            result["14-identify-bottleneck"] = 1
    except:
        pass

    try:
        content = (d / "q2.txt").read_text()
        answer = content.split()
        if "no" in answer and "yes" not in answer:
            result["15-identify-memory"] = 1
    except:
        pass

    try:
        f = (d / "htop-screenshot-1.pdf")
        expected = "/stat129/class/skills/scratch/htop-screenshot-1.pdf"
        if filecmp.cmp(f, expected):
            result["16-transfer-files"] = 1
    except:
        pass

    try:
        f = (d / "q4.txt")
        expected = "/stat129/class/skills/scratch/02-24-4.out"
        if filecmp.cmp(f, expected):
            result["17-parallelize"] = 1
    except:
        pass

    return result


standards = """
    14-identify-bottleneck
    15-identify-memory
    16-transfer-files
    17-parallelize
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
