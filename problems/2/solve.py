
fib_nums = [1,2]
a = 1
b = 2
c = 0
while c <= 4000000:
  c = a + b
  if c > 4000000:
    break
  else:
    fib_nums.append(c)
    a = b
    b = c

result = 0
for n in fib_nums:
  if n % 2 == 0:
    result += n

print result
