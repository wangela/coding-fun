def walk_hex_grid(steps):
    # Parameter: steps is a list of steps the child took in the hex grid
    # Output: An integer, the fewest number of steps required to reach the child
    shortest = 0
    north = 0
    east = 0

    for step in steps:
        if step == "n":
            step = "nn"
        elif step == "s":
            step = "ss"

        for direction in step:
            if direction == "n":
                north += 1
            elif direction == "s":
                north -= 1
            elif direction == "e":
                east += 1
            elif direction == "w":
                east -= 1

    # Every step horizontally is a diagonal step, so subtract a vertical for every horizontal
    diagonal = abs(east)
    vertical = abs(north) - abs(east)
    extra_vertical = vertical % 2 # This should not happen
    vertical //= 2

    shortest = diagonal + vertical

    return shortest

def wander_hex_grid(steps):
    # Parameter: steps is a list of steps the child took in the hex grid
    # Output: An integer, the farthest he got
    shortest = 0
    north = 0
    east = 0
    furthest = 0

    for step in steps:
        if step == "n":
            step = "nn"
        elif step == "s":
            step = "ss"

        for direction in step:
            if direction == "n":
                north += 1
            elif direction == "s":
                north -= 1
            elif direction == "e":
                east += 1
            elif direction == "w":
                east -= 1

        # Every step horizontally is a diagonal step, so subtract a vertical for every horizontal
        diagonal = abs(east)
        vertical = abs(north) - abs(east)
        extra_vertical = vertical % 2 # This should not happen
        vertical //= 2

        shortest = diagonal + vertical

        if shortest > furthest:
            furthest = shortest

    return furthest
