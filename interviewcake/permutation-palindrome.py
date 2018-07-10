def can_has_palindrome(A):
    # Parameter: A is a string
    # Perform: Can a permutation of A be a palindrome?
    # Output: True/False
    unmated = set()

    for letter in A:
        if letter in unmated:
            unmated.remove(letter)
        else:
            unmated.add(letter)
        print(unmated)

    if len(unmated) > 1:
        return False
    else:
        return True
