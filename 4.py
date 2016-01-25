"""
https://projecteuler.net/problem=4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9000 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import os, sys, inspect
# Why is this so hard?
step1 = inspect.currentframe()
step2 = inspect.getfile(step1)
step3 = inspect.getfile(step2)
step4 = os.path.split(step3)[0]
step5 = os.path.join(step4,"tools")
step6 = os.path.abspath(step5)
cmd_subfolder = os.path.realpath(step6)
if cmd_subfolder not in sys.path:
     sys.path.insert(0, cmd_subfolder)
import palindrome

winner = 0
for n in range(900):
  for k in range(n,900):
    candidate = (999 - n) * (999 - k)
    if candidate > winner:
      if palindrome.is_palindrome(candidate):
        winner = candidate

print winner
