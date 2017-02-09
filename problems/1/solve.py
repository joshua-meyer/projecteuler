
multiples = []
for n in range(1,1001):
  if n % 3 == 0 or n % 5 == 0:
    multiples.append(n)

result = 1
for n in multiples:
  result *= n

print result
