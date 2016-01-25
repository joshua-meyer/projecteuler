def is_palindrome(number):
  n = list(str(number))
  while True:
    if len(n) in [0,1]:
      return True
    if n.pop() != n.pop(0):
      return False
