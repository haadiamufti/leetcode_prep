# Write a function, get_node_value, that takes in the head of a linked list and an index. The function should 
# return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

class Node:
      def __init__(self, val):
        self.val = val
        self.next = None

# def get_node_value(head, index):
#   current = head
#   i = 0
#   while current is not None:
#     if i == index:
#       return current.val
#     current = current.next
#     i += 1
#   return None


def get_node_value(head, index):
  if head is None:
    return None
  elif index == 0:
    return head.val
  return get_node_value(head.next, index-1)
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 7)) # None

