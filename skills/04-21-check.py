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

    d = Path("/home/{}/skills/04-21".format(name))

    try:
        #set_trace()
        code = (d / "genclusters.py").read_text().strip()
        m1 = re.search(r'KMeans(.*3.*)', code)
        m2 = re.search(r'y2\s*=.*fit_predict(.*)', code)
        if m1 and m2:
            result["26-kmeans-fit"] = 1
    except:
        pass

    try:
        with open(d / "y.csv") as file:
            reader = csv.reader(file)
            values = " ".join(r[1] for r in reader)
        if values == "count 1667 1667 1666":
            result["27-counter"] = 1
    except:
        pass

    return result


standards = """
    26-kmeans-fit
    27-counter
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
