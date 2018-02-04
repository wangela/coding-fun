def find_missing_drone(deliveryIdConfirmations):
    # Parameter: deliveryIdConfirmations is a list of IDs entered once if taken off and once when returned
    # Output: The one ID that does not have a duplicate
    # Example: [1, 2, 3, 4, 5, 6, 1, 2, 4, 5, 6]
    # 0001
    # 0010
    # 0011
    # 0100
    # 0101
    # 0110
    # 0001
    # 0010
    # 0100
    # 0101
    # 0110

    test = 0
    for each in deliveryIdConfirmations:
        test ^= each

    return test
