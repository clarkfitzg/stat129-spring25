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

from IPython.core.debugger import set_trace

from mystery import mystery_number



def score(name, standards):
    """score standards based on first name
    """
    result = {s: 0 for s in standards}
    result["name"] = name

    d = Path("/home/{}/skills/03-12".format(name))

    try:
        content = (d / "q1.txt").read_text().strip()
        expected = str(mystery_number(name))
        if content == expected:
            result["19-run-python-interactive"] = 1
    except:
        pass

    try:
        code = open(d / "convert-temp.py").read()
        exec(code)
        c40 = locals()["c_to_f"](40)
        if c40 == 104:
            result["20-define-function"] = 1
    except:
        pass

    #set_trace()
    return result


standards = """
    19-run-python-interactive
    20-define-function
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
