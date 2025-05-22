# You are designing a waitlist system for a restaurant. The system needs to support the 
# following operations:






# Additional constraints:

# There are only 10 unique table sizes, ranging from 1 to 10.

# Customer names are unique.

# Multiple parties may have the same size, but names are unique.

# All operations should be reasonably efficient.
from collections import OrderedDict, defaultdict
class RestarauntWaitlist:
    
    def __init__(self):
        self.cus_queue = defaultdict(OrderedDict)
        self.cus_dict = {}
    
    # Add a customer party to the waitlist. Each party has a unique customer name and a party size.
    # Example: "Bob", party of 4
    def add(self, name, size):
        self.cus_queue[size][name]=None
        self.cus_dict[name]=size
        
    # Remove a customer from the waitlist by name (e.g., if they leave or cancel).
    def remove(self, name):
        if name in self.cus_dict:
            size = self.cus_dict[name]
            del self.cus_dict[name]
            del self.cus_queue[size][name]
            
    
    # When a table becomes available with N seats, return and remove the first party from the waitlist with exactly N people.

    # If no matching party exists, return null (or equivalent).

    # If multiple parties match the table size, the earliest one added (FIFO) should be selected.
    def get_next_party(self, size):
        if self.cus_queue[size]:
            name,_ = self.cus_queue[size].popitem(last=False)
            del self.cus_dict[name]
            return (name,size)
            
        return None