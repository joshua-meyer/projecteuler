"""
https://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import os, sys, inspect
# Why is this so hard?
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"tools")))
if cmd_subfolder not in sys.path:
     sys.path.insert(0, cmd_subfolder)
import prime_generator

p = prime_generator.first_primes(10001)

print p[10000]
