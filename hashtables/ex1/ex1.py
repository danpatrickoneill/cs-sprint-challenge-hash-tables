def get_indices_of_item_weights(weights, length, limit):
    weights_table = {}
    for i, weight in enumerate(weights):
        weights_table[weight] = (limit - weight, i)
        if i == 0:
            continue
        if limit - weight in weights_table:
            if weight == limit - weight:
                return (weights_table[weight][1], weights.index(weight))
            return (weights_table[weight][1], weights_table[limit-weight][1])
        

    return None

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

print(answer_2)