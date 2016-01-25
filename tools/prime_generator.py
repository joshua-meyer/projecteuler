def next_prime(primes = []):
  if primes == []:
    return 2
  next_prime = max(primes) + 1
  not_done = True
  while not_done:
    for p in primes:
      if next_prime % p == 0:
        next_prime += 1
        break
    else:
      not_done = False
  return next_prime

def primes_under(cap):
  primes = []
  max_prime = 0
  while max_prime < cap:
    max_prime = next_prime(primes)
    if max_prime >= cap:
      return primes
    else:
      primes.append(max_prime)

def is_prime(x):
  primes = []
  max_prime = 0
  while max_prime < x:
    max_prime = next_prime(primes)
    print max_prime
    if max_prime == x:
      return True
    elif max_prime > x:
      return False
    else:
      primes.append(max_prime)
  else:
    return False

def first_primes(n):
  i = 0
  primes = []
  while i < n:
    primes.append(next_prime(primes))
    i += 1
  return primes

def decompose(n):
  k = n
  primes = []
  factors = {}
  while k > 1:
    new_prime = next_prime(primes)
    while k % new_prime == 0:
      if new_prime in factors:
        factors[new_prime] += 1
      else:
        factors[new_prime] = 1

      k /= new_prime

    if new_prime > k and k > 1:
      print "ERROR: stuck at %s" % k
      break
    primes.append(new_prime)

  return factors

def least_common_multiple(numbers):
  factors = {}
  for number in numbers:
    factorization = decompose(number)
    for factor in factorization:
      if not factor in factors:
        factors[factor] = factorization[factor]
      elif factorization[factor] > factors[factor]:
        factors[factor] = factorization[factor]

  result = 1
  for factor in factors:
    result *= factor ** factors[factor]

  return result

def number_of_divisors(n):
  prime_factors = decompose(n)
  num = 1
  for p in prime_factors:
    num *= (prime_factors[p] + 1)
  return num
