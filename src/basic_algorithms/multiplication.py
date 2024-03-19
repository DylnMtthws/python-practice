#RECURSIVE

def multiplication(num_1, num_2):
  if num_1 < 1 or num_2 < 1:
    return 0
  new_num = num_2 - 1
  return num_1 + multiplication(num_1, new_num)

print(multiplication(2,8))
# test cases
# print(multiplication(3, 7) == 21)
# print(multiplication(5, 5) == 25)
# print(multiplication(0, 4) == 0)

#ITERATIVE

def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

multiplication(3, 7)
# 21
multiplication(5, 5)
# 25
multiplication(0, 4)
# 0
