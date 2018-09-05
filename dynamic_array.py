#!/bin/python3

import math
import os
import random
import re
import sys

def find_sequence(last_answer, seq_list, x):
    index = (x ^ last_answer) % len(seq_list)
    seq = seq_list[index]
    if seq is None:
        seq_list[index] = []
        seq = seq_list[index]
    return seq

def query_one(last_answer, seq_list, x, y):
    """ performs query one """
    seq = find_sequence(last_answer, seq_list, x)
    seq.append(y)
    return last_answer
    
def query_two(last_answer, seq_list, x, y):
    """ performs query two"""
    seq = find_sequence(last_answer, seq_list, x)
    last_answer = seq[y % len(seq)]
    print(last_answer)
    return last_answer

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    answers = []
    last_answer = 0
    seq_list = [None] * n
    for query in queries:
        function = query_one if query[0] == 1 else query_two
        last_answer = function(last_answer, seq_list, query[1], query[2])
        if query[0] == 2:
            answers.append(last_answer)
        
    return answers
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
