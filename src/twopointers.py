from linkedlist import LinkedList

# Two pointers moving at the SAME speed (not alway optimal)
def nth_last_node(linked_list, n):
    nth_pointer = None
    lead_pointer = linked_list.head_node
    count = 1
    while lead_pointer:
        lead_pointer = lead_pointer.get_next_node()
        count += 1
        if count >= n + 2: # Corrected condition
            
            if nth_pointer is None:
                nth_pointer = linked_list.head_node
            else:
                nth_pointer = nth_pointer.get_next_node()
    return nth_pointer

#Fast pointer moves two spaces for every one space of slow pointer
def find_middle(linked_list):
  fast_pointer = linked_list.head_node
  slow_pointer = linked_list.head_node

  while fast_pointer:
    fast_pointer = fast_pointer.get_next_node()
    if fast_pointer != None:
      fast_pointer = fast_pointer.get_next_node()
      slow_pointer = slow_pointer.get_next_node()
  return slow_pointer

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print('4th to last value', nth_last.value)
middle_node = find_middle(test_list)
print("Middle node: ", middle_node.value)
