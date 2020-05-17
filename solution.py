"""Return maximum profit with least weight."""



def find_least_valued_and_most_heavy_item(items):
    """Find the 'worst' item.
        (ex)

        items in := ["Spoon": weight 10, value 10, Phone: weight 100, value 10000]

        worst out:= "Spoon"       

    """

    least = items[0]
    for item in items:
        if item.val < least.val and item.weight > item.weight:
            least = item
    return least

def solve_with_items(current_items, max_weight, items_to_choose_from):
    pass

def solve_from_empty(items, max_weight):
    """With (a few) given items, what are the best to take."""
    total_value, total_weight = 0, 0
    
    for item in items:
        total_weight += item.weight
        total_value += item.val
    
    if total_weight <= max_weight:
        return items
    
    else:
        while total_weight > max_weight:
            least_valued_and_most_heavy_item = find_least_valued_and_most_heavy_item(items)