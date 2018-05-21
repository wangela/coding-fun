def reverse_words(A):
    # Parameter: A is a list of characters where one space separates words and
    #   there are only letters and spaces
    # Perform: Reverse the order of the words in-place
    # Output: The resulting reversed string
    # Example: ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']
    #   -> ['steal', 'pound', 'cake']
    # Approaches:
    #   Naive: Move each character to the beginning until reaching a space.
    #       Then, update "end" to the index before the last start.
    #       Subtract one from new start index every move
    #       O(n) time, O(1) space
    if len(A) == 0:
        return []
    word_length = 0
    current_start = 0
    current_word = ''
    current_letter = A.pop()
    current_index = len(A) - 1
    while current_index > -1:
        if current_letter != ' ':
            A.insert(current_start, current_letter)
            word_length += 1
            current_index -= 1
            current_letter = A.pop()
        if current_letter == ' ':
            current_start += word_length
            A.insert(current_start, current_letter)
            current_start += 1
            word_length = 0
            current_index -= 1
            current_letter = A.pop()

    A.insert(current_start, current_letter)

    return A
