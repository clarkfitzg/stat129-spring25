#!/usr/bin/env python3
"""
Sum integers from stdin
"""

from sys import stdin

total = 0
for line in stdin:
    total = total + line

print(total)
