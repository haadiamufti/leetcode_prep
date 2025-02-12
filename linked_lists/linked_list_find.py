class Node:
      def __init__(self, val):
        self.val = val
        self.next = None

# def linked_list_find(head, target):
#   current = head
#   while current is not None:
#     if current.val == target:
#       return True
#     current = current.next 
#   return False

def linked_list_find(head, target):
  if head is None:
    return False
  return head.val == target or linked_list_find(head.next, target)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_find(a, "q") )# False

