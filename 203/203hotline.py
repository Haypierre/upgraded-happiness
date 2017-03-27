#!/usr/bin/env python3

import sys
import time
import math

usage = """USAGE\n                       ./203hotline[n k | d]
DESCRIPTION
\tn\tn value for the computation of Combination n, k
\tk\tk value for the computation of Combination n, k
\td\taverage duration of calls(in seconds)"""

overload = 0

def nb_combination(n, k):
    if (k < 0 or n < 0 or k > n):
        sys.exit(84)
    return (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def binomial(k, p, n):
    return (nb_combination(n, k) *  math.pow(p, k) * math.pow(1 - p, n - k))

def poisson(k, p, *unused):
    return (math.exp(-p) * pow(p, k) / math.factorial(k))

def print_stat(beg):
    print("\noverload: ", "%0.1f" % (overload * 100), "%", sep='')
    print("computation time:", "%0.2f" % ((time.time() - beg) * 1000), "ms")

def print_result(fcnt, p):
    global overload
    if fcnt == "poisson":
        p *= 3500
    for k in range(50):
        result = globals()[fcnt](k, p, 3500)
        if k <= 25:
            overload += result
        if k and (k + 1) % 6 == 0:
            print(k, "->", "%0.3f " % result, sep='')
        else:
            print(k, "->", "%0.3f " % result, end='\t', sep='')
    result = globals()[fcnt](k + 1, p, 3500)
    overload = 1 - overload
    print(k + 1, " -> ", "%0.3f", % result, sep='')

            
if len(sys.argv) == 3:
    try:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
    except ValueError:
        sys.exit(84)
    result = int(nb_combination(n, k))
    print(k , "-combination of a ", n, " set:\n", result, sep='')

elif len(sys.argv) == 2:
    if sys.argv[1] == '-h':
        print (usage)
        sys.exit(84)
    try:
        d = int(sys.argv[1])
    except ValueError:
        sys.exit(84)
    print ("Binomial distribution:")
    p = d / 3600.00 / 8.00
    beg = time.time()
    print_result("binomial", p)
    print_stat(beg)
    print ("\nPoisson distribution:")
    beg = time.time()
    overload = 0
    print_result("poisson", p)
    print_stat(beg)
else:
    sys.exit(84)
