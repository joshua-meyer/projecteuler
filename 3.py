"""
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import os, sys, inspect
# Why is this so hard?
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"tools")))
if cmd_subfolder not in sys.path:
     sys.path.insert(0, cmd_subfolder)
import prime_generator

factors = prime_generator.decompose(600851475143)

factor_list = []
for prime in factors:
  factor_list.append(prime)

print max(factor_list)
