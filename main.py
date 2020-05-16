"""The nabsack problem.

#Idea 1
We'll add all items to our sack.
Then, if it fits in, we'll keep them all
otherwise, we'll keep removing the least valueble, and most heavy item until we are "proper"


Psuedo Code.

class item
    value
    weight

    func greater(this, other)
        if this.value > other.value && this.weight < other.weight // We prefer more valueble, and less heavy objects
            true
        otherwise,
            false
    


items = item('Spoon', value=10, weight=3), item('TV', value=1000, weight=3500)
wrintln "the best is best(items)"

// Other thing

current_items = item('Spoon', value=10, weight=3), item('TV', value=1000, weight=3500) & max_weight = 4000
"""

from generate_word import words
from solution import *

class Item():
    """Base class for all our items."""

    def __init__(self, name, val, weight):
        """Init the item."""
        self.weight = weight
        self.name = name
        self.val = val

    def __ge__(self, other, type='val'):
        """Compare wether or not an item has more value OR less weight than an other."""
        if type == 'val':
            if self.val > other.val:
                return True
            return
        elif type == 'weight':
            if self.weight < other.weight:
                return True
            return
        else:
            print(f'Unkown type \'{type}\' ')
            return

    def __eq__(self, other):
        """Is the current object the same as an other."""
        if self.val == other.val and self.weight == other.weight:
            return True
        return

    def __repr__(self):
        """Represent the item."""
        return f"<{self.name}, value: {self.val}, weight: {self.weight}>"

    def __str__(self):
        """Represent the item in string format."""
        return f"<{self.name}, value: {self.val}, weight: {self.weight}>"


items = [Item('Spoon', 10, 10), Item('Table', 30, 100)]