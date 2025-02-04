#!/usr/bin/env python3
import csv
import filecmp
import os
import sys
from pathlib import Path


def record(name, writer):
    """Record scores based on first name
    """
    score = {"name": name,
             "01-ssh-server": 0,
             "02-read-file": 0,
             "03-make-directory": 0,
             "04-list-files": 0,
             "05-redirect-output": 0,
             }

    d = Path("/home/{}/skills/02-03".format(name))

    if d.is_dir():
        score["01-ssh-server"] = 1
        score["02-read-file"] = 1
        score["03-make-directory"] = 1

    f = d / "q3.txt"
    try:
        if filecmp.cmp(f, "/home/fitzgerald/02-03.out"):
            score["04-list-files"] = 1
            score["05-redirect-output"] = 1
    except:
        pass
    writer.writerow(score)


names = os.listdir("/home")
fields = "name,01-ssh-server,02-read-file,03-make-directory,04-list-files,05-redirect-output".split(",")
writer = csv.DictWriter(sys.stdout, fields)
writer.writeheader()

for name in names:
    record(name, writer)
