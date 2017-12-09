def pick_movies(flight_length, movie_lengths):
    # Parameters:
    #   flight_length is an integer for the minutes of the flight
    #   movie_lengths if an array of integers for the minutes of each movie
    # Output: True or False whether there are two movies whose sum equals flight_length
    #   Don't watch the same movie twice
    #   Optimize for runtime over memory

    movie_options = set(movie_lengths)

    for index, each in enumerate(movie_lengths):
        remainder = flight_length - each
        if remainder in movie_options:
            if remainder != each:
                return True
            else:
                rest_of_movies = set(movie_lengths[index + 1:])
                if remainder in rest_of_movies:
                    return True

    return False

# O(n) time and O(n) space
