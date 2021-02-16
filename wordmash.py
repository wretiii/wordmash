#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import itertools

# empty list is declared for the list found in the first input file
inputlist1 = []

# pull each line from the first input file and strip trailing whitespace
for file1 in sys.argv[1:]:
    words1 = []
    with open(file1) as fp1:
        for line in fp1:
            words1.append(line.rstrip())
    inputlist1.append(words1)

# pull each line from the second input file and strip trailing whitespace
for file2 in sys.argv[2:]:
    words2 = []
    with open(file2) as fp2:
        for line in fp2:
            words2.append(line.rstrip())

# print wordmash wordlist
for wordmash in itertools.product(*inputlist1):
    print("".join(wordmash))