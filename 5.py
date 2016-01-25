"""
https://projecteuler.net/problem=5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import os, sys, inspect
# Why is this so hard?
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"tools")))
if cmd_subfolder not in sys.path:
     sys.path.insert(0, cmd_subfolder)
import prime_generator

lcm = prime_generator.least_common_multiple(range(1,21))
print lcm
