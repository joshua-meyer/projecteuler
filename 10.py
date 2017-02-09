"""
https://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from tools import prime_generator

print "Takes like, 20 minutes."

primes = prime_generator.primes_under(2000000)

total = 0
for p in primes:
  total += p

print total
