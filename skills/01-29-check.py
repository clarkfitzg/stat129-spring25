#!/usr/bin/env python3
from pathlib import Path
import filecmp

skills = Path.home() / "skills"
if skills.is_dir():
    print("Q1 correct")
else:
    print("Q1 try again")


d = skills / "01-29"
if d.is_dir():
    print("Q2 correct")
else:
    print("Q2 try again")


f = d / "q3.txt"
if filecmp.cmp(f, "/stat129/class/skills/scratch/01-29.out"):
    print("Q3 correct")
else:
    print("Q3 try again")
