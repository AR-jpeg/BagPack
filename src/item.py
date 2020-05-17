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