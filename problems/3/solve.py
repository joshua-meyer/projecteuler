
from tools import prime_generator

factors = prime_generator.decompose(600851475143)

factor_list = []
for prime in factors:
  factor_list.append(prime)

print max(factor_list)
