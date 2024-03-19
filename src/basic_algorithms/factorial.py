#ITERATIVE
def factorial(n):
  if n < 0:
    return ValueError('Inputs 0 or greater only')
  elif n <= 1:
    return 1
  else:
    result = 1
    while n != 0:
      result = result * n
      n -= 1
    return result

# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)


#RECURSIVE
# runtime: Linear - O(N)
def factorial(n):  
  if n < 0:    
    return ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)

factorial(3)
# 6
factorial(4)
# 24
factorial(0)
# 1
factorial(-1)
# ValueError "Input must be 0 or greater"
