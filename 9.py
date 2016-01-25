"""
https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

solution = []

done = False
for a in range(1,998):
  for b in range(a,1000 - a):
    c = 1000 - a - b
    if a ** 2 + b ** 2 == c ** 2:
      solution.append([a,b,c])

# print solution

if len(solution) == 1:
  result = 1
  for n in solution[0]:
    result *= n
  print result
else:
  print "ERROR: More than 1 solution exits!"
