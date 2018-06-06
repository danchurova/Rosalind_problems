#!/usr/bin/env python2

def main():
    input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    sumA = 0
    sumC = 0
    sumG = 0
    sumT = 0

    for x in input:
        if x == 'A':
            sumA += 1
        if x == 'C':
            sumC += 1
        if x == 'G':
            sumG += 1
        if x =='T' :
            sumT += 1
    print sumA, sumC, sumG, sumT


main()
