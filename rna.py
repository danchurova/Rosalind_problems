#!/usr/bin/env python2

import sys

input = 'GATGGAACTTGACTACGTAAATT'
output = ''

for x in input:
    if x == 'A':
        output += 'U'
    if x == 'C':
        output += 'G'
    if x == 'G':
        output += 'C'
    if x == 'T':
        output += 'A'

print output

