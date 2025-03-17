#!/usr/bin/env python3
"""
Copy the 2023 files into a directory.
"""
import os
import shutil

all990 = os.listdir("/stat129/all990files/")

tax23 = [f for f in all990 if f.startswith("2023")]
for f in tax23:
    shutil.copy("/stat129/all990files/" + f,
                "/stat129/tax23/" + f)
