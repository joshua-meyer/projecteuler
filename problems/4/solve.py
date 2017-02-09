
from tools import palindrome

winner = 0
for n in range(900):
  for k in range(n,900):
    candidate = (999 - n) * (999 - k)
    if candidate > winner:
      if palindrome.is_palindrome(candidate):
        winner = candidate

print winner
