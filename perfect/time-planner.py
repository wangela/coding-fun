# Clumsy solution
def meeting_planner(slotsA, slotsB, dur):
    # Parameters: slotsA, slotsB are available time slots in format
    #   [[start, end], [start, end]...[start, end]]
    #   where start and end are in epoch time. dur is a duration in seconds.
    # Output: The first time slot that will work in format [start, end]
    later_start = 0
    final_end = 0
    earlier_index = 0
    later_index = 0
    earlier_person = None
    later_person = None

    # Check for length and overlap
    if len(slotsA) == 0 or len(slotsB) == 0 or dur <= 0:
        return []
    last_end_a = slotsA[-1][1]
    last_end_b = slotsB[-1][1]
    first_end = min(last_end_a, last_end_b)

    first_start_a = slotsA[0][0]
    first_start_b = slotsB[0][0]
    later_start = max(first_start_a, first_start_b)

    if first_end < later_start:
        return []

    # 1. Find first possibly overlapping start by picking the later start time
    if first_start_a > first_start_b:
        later_person = slotsA
        earlier_person = slotsB
    else:
        later_person = slotsB
        earlier_person = slotsA

    # 2. Determine if there's an overlap by checking if the opposite end time is later
    while later_index < len(later_person) and earlier_index < len(earlier_person):
        later_start = later_person[later_index][0]
        later_person_end = later_person[later_index][1]
        earlier_person_end = earlier_person[earlier_index][1]
        if earlier_person_end >= later_start: # There is an overlap
            overlap = min(later_person_end, earlier_person_end) - later_start
            if overlap >= dur:                # Overlap satisifes the duration; found our answer
                final_end = later_start + dur
                return [later_start, final_end]
            else:                               # The overlap was too small; figure out if there is another start worth trying
                if earlier_index == len(earlier_person) - 1 and later_index + 1 < len(later_person):
                    if later_person[later_index + 1][0] < earlier_person[-1][1]:
                        later_index += 1
                    else:
                        return []
                elif later_index == len(later_person) and earlier_index + 1 < len(earlier_person):
                    if earlier_person[earlier_index + 1][0] < later_person[-1][1]:
                        earlier_index += 1
                        temp_index = earlier_index
                        earlier_index = later_index
                        later_index = temp_index
                        temp = earlier_person
                        earlier_person = later_person
                        later_person = temp
                    else:
                        return []
                elif earlier_person[earlier_index + 1][0] < later_person[later_index + 1][0]:
                    earlier_index += 1
                    temp_index = earlier_index
                    earlier_index = later_index
                    later_index = temp_index
                    temp = earlier_person
                    earlier_person = later_person
                    later_person = temp
                else:
                    later_index += 1
        else:                                   # No overlap; move opposite to next start which may be either person
            earlier_index += 1
            if earlier_person[earlier_index][0] > later_start: # Earlier is now the later start
                temp_index = earlier_index
                earlier_index = later_index
                later_index = temp_index
                temp = earlier_person
                earlier_person = later_person
                later_person = temp

    # If while loop has exited, we've reached the end of someone's availabilities
    # without finding a satisfactory overlap.
    return []

# Streamlined solution
def meeting_planner(slotsA, slotsB, dur):
    # Parameters: slotsA, slotsB are available time slots in format
    #   [[start, end], [start, end]...[start, end]]
    #   where start and end are in epoch time. dur is a duration in seconds.
    # Output: The first time slot that will work in format [start, end]
    index_a = 0
    index_b = 0

    while index_a < len(slotsA) and index_b < len(slotsB):
        start = max(slotsA[index_a][0], slotsB[index_b][0])
        end = min(slotsA[index_a][1], slotsB[index_b][1])

        if start + dur <= end:
            return [start, start + dur]

        if slotsA[index_a][1] < slotsB[index_b][1]:
            index_a += 1
        else:
            index_b += 1

    return []
