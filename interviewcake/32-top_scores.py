def top_scores(unsorted_scores, highest_possible_score):
    # Parameters:
    #   unsorted_scores is an unsorted list of integers (scores)
    #   highest_possible_score is an integer
    # Output:
    #   Return a list of sorted scores from highest to lowest
    # Complexity goal:
    #   Faster than O(n log n)  time
    # Example: [37, 89, 41, 65, 91, 53], 100 -> [91, 89, 65, 53, 41, 37]
    # Approach:
    #   Quicksort and Mergesort are both O(n log n) which uses recursive left and right sorting
    #   To get faster, we have to aim for O(n) time.
    #   Build a dict of all scores between 1 to highest and count number at each score

    score_counts = [0] * (highest_possible_score + 1)

    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []

    for score in xrange(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        for time in xrange(count):
            sorted_scores.append[score]

    return sorted_scores

# O(n) time and O(n) space
