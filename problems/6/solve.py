
sum_of_squares = 0
for n in range(1,101):
  sum_of_squares += n ** 2

just_sum = 0
for n in range(1,101):
  just_sum += n
square_of_sum = just_sum ** 2

print square_of_sum - sum_of_squares
