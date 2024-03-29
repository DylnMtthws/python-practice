#RECURSIVE

def find_min(my_list, min=None):
  if len(my_list) == 0:
    return min
  else:
    if min == None or my_list[0] < min:
      min = my_list[0]
  return find_min(my_list[1:], min)



# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)

#ITERATIVE
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min

find_min([42, 17, 2, -1, 67])
# -1
find_mind([])
# None
find_min([13, 72, 19, 5, 86])
# 5
