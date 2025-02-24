#!/usr/bin/env python3
"""
Sum integers from stdin
"""

from sys import stdin

# First collect all the numbers a big list
numbers = [int(x) for x in stdin]

print(sum(numbers))


