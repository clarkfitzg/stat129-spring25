#!/bin/bash
# ^ That is called the "shebang" line

zcat $1 | grep "TMAX" | head
