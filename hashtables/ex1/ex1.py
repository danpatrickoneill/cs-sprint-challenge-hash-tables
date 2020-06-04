def get_indices_of_item_weights(weights, length, limit):
    weights_table = {}
    # Deals with false positives from half-limit weights finding themselves
    found_half = False
    for i, weight in enumerate(weights):
        weights_table[weight] = (limit - weight, i)
        # The first time we find a half-limit weight, jump to the next step in the loop without checking table
        if weight == limit - weight and found_half is False:
            found_half = True
            continue
        if limit - weight in weights_table:
            if weight == limit - weight:
                return (weights_table[weight][1], weights.index(weight))
            return (weights_table[weight][1], weights_table[limit-weight][1])
        

    return None

weights_2 = [2, 2, 4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 4, 8)

print(answer_2)