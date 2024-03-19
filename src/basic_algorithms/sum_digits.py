#RECURSIVE
def sum_digits(n):
  if n < 0:
    ValueError('Inputs 0 or greater only')
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits((n // 10)) + last_digit

# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)

#ITERATIVE
# Linear - O(N), where "N" is the number of digits in the number
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

sum_digits(12)
# 1 + 2
# 3
sum_digits(552)
# 5 + 5 + 2
# 12
sum_digits(123456789)
# 1 + 2 + 3 + 4...
# 45
