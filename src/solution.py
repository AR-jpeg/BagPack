"""Return maximum profit with least weight."""



def find_least_valued_and_most_heavy_item(items):
    """Find the 'worst' item.
        (ex)

        items in := ["Spoon": weight 10, value 10, Phone: weight 100, value 10000]

        worst out:= "Spoon"       

    """

    least = items[0]
    for item in items:
        if item.score < least.score:
            least = item
    return least

def solve_with_items(current_items, max_weight, items_to_choose_from):
    pass

def solve_from_empty(items, max_weight):
    """With (a few) given items, what are the best to take."""
    total_value, total_weight, end = 0, 0, []
    
    for item in items:
        total_weight += item.weight
        total_value += item.val
        end.append(item)
    
    # Are we 'ok'
    if total_weight <= max_weight:
        return items
    
    else:
        while total_weight > max_weight:
            least_valued_and_most_heavy_item = find_least_valued_and_most_heavy_item(items)
            end.remove(least_valued_and_most_heavy_item)
            print("Least valued and most heavy item:", least_valued_and_most_heavy_item.name)
            total_value -= least_valued_and_most_heavy_item.val
            total_weight -= least_valued_and_most_heavy_item.weight
    
            return end