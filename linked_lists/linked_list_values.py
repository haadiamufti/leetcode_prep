# Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
# The function should return a list containing all values of the nodes in the linked list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_values(head):
  linked_list_values = []
  current = head
  while current != None:
    linked_list_values.append(current.val)
    current = current.next
  return linked_list_values
    
q = Node("q")

# q

linked_list_values(q) # -> [ 'q' ]


# a -> b -> c -> d

print(linked_list_values(q) )# -> [ 'a', 'b', 'c', 'd' ]
