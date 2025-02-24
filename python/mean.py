#!/usr/bin/env python3
"""
Sum integers from stdin
"""

from sys import stdin

n = 0
total = 0
for line in stdin:
    total = total + int(line)
    n = n + 1

print(total / n)


