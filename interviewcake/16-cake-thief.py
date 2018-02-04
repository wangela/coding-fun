def max_duffel_bag_value(cakes, capacity):
    # Parameters: A list of cake type tuples (weight integer, value integer)
    #   and a weight capacity of the bag
    #   Weights >= 0, Values >= 0
    # Output: An integer, the maximum monetary value the bag can hold
    # Example: [(7, 180), (3, 90), (2, 15)], 20 -> 555 (6*[1] + 1*[2])
    # Consider case where it makes more sense to fill with the 7-lb cake instead
    #   of another 3-lb cake... 3*6 = 540$ vs 3*4 = $360 + 1*7 = $190 = $550
    max_values_for_capacities = [0] * (capacity + 1)

    if capacity == 0:
        return 0
    for x in range(capacity + 1):
        current_max = 0
        for cake in cakes:
            current_weight = cake[0]
            current_value = cake[1]
            if current_weight == 0:
                if current_value > 0:
                    return sys.maxint
                else:
                    continue
            if current_weight <= x:
                current_cake_value_add = max_values_for_capacities[x - current_weight] + current_value
                current_max = max(current_max, current_cake_value_add)
        max_values_for_capacities[x] = current_max

    return max_values_for_capacities[capacity]
