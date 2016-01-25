"""
https://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import os, sys, inspect
# Why is this so hard?
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"tools")))
if cmd_subfolder not in sys.path:
     sys.path.insert(0, cmd_subfolder)
import prime_generator

print "Takes like, 20 minutes."

primes = prime_generator.primes_under(2000000)

total = 0
for p in primes:
  total += p

print total
