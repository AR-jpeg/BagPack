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

from solution import solve_from_empty #, solve_with_items
from generate_word import words
from item import Item


items = [Item('Spoon', val=100, weight=10), Item('Table', 99, 100)]

best_items_from_empty = solve_from_empty(items, 100)

print("'Best' items from empty:", end=' ')
for item in best_items_from_empty:
    print(item, end=', ')
print()