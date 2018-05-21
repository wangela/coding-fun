import os
def find_duplicates():
    # Output: List of tuples where the first element is the duplicate filepath
    #   and the second element is the original filepath.
    filenames = os.listdir("data")
    filepairs = {}
    for each in filenames:
        file = open(each)
        if each in filepairs:
            # Figure out which one is the duplicate by comparing creation date
        else: # Check if path is same
            filepairs.add(each)
