#!/bin/python3

import math
import os
import random
import re
import sys


def dynamicArray(n, q):
    result=[]
    last_ansr=0
    seq = [ [] for j in range(n) ]
    for i in range(0,len(q)):
        xor=(q[i][1]^last_ansr)
        s=xor%n
        if(q[i][0]==1):
            seq[s].append(q[i][2])
        else:
            value=q[i][2]%len(seq[s])
            last_ansr=seq[s][value]
            result.append(last_ansr)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
