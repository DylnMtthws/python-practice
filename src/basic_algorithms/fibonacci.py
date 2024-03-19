#ITERATIVE 
def fibonacci(n):
  if n < 0:
    ValueError('Input 0 or greater only')
  elif n <= 1:
    return n
  else:
    fibs_list = [0, 1]
    if n <= (len(fibs_list) - 1):
      return fibs_list[n]
    else:
      while n > (len(fibs_list) - 1):
        next_fib = fibs_list[-1] + fibs_list[-2]
        fibs_list.append(next_fib)
      return fibs_list[n]

# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)


#RECURSIVE

# runtime: Exponential - O(2^N)

def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
# 2
fibonacci(7)
# 13
fibonacci(0)
# 0
