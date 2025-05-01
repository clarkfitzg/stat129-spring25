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

from IPython.core.debugger import set_trace


def score(name, standards):
    """score standards based on first name
    """
    result = {s: 0 for s in standards}
    result["name"] = name

    d = Path("/home/{}/skills/04-30".format(name))

    try:
        code = (d / "read-student.py").read_text().replace(" ", "")
        m1 = re.search(r"student\[.?courses.?\]\[0\]\[.?grades.?\]\[.?final.?\]", code)
        if m1:
            result["28-nested-JSON"] = 1
    except:
        pass

    try:
        content = (d / "q2.txt").read_text()
        #set_trace()
        m1 = re.search(r"^Response:", content)
        m2 = re.search(r"[0-9.]\s*[R|Python]", content)
        if m1 and m2:
            result["29-LLM-Python"] = 1
    except:
        pass

    return result


standards = """
    28-nested-JSON
    29-LLM-Python
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
