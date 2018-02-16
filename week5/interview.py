def combo_cost(n, c_lib, c_road):
    cost = c_lib
    cost += (n - 1) * c_road
    return cost

def libraries_cost(n, c_lib):
    cost = n * c_lib
    return cost

def roadsAndLibraries(n, c_lib, c_road, possible_roads):
    minimum_total_cost = 0

    # Form adjacency matrix out of possible_roads
    adjacent = []
    for i in range(n):
        adjacent.append([])

    for pair in possible_roads:
        adjacent[pair[0] - 1].append(pair[1] - 1)
        adjacent[pair[1] - 1].append(pair[0] - 1)

    # Identify separate states and count the number of cities in each state
    states = [] # Int of number of cities in that state (connected graph)
    visited = [False] * n # Boolean

    for city in range(n):
        state_size = 0
        if not visited[city]:
         dfs = []
         dfs.append(city)
         visited[city] = True

         while len(dfs) > 0:
             count_city = dfs.pop()
             state_size += 1

             adj_cities = adjacent[count_city]
             for ac in adj_cities:
                 if !visited[ac]:
                     dfs.append(ac)
                     visited[ac] = True

         states.append(state_size)

    for state in states:
        # Determine roads + library cost
        combination_cost = combo_cost(state, c_lib, c_road)

        # Determine the libraries-only cost
        libs_cost = libraries_cost(state, c_lib)
        # Determine the minimum cost
        state_cost = min(combination_cost, library_cost)

        # Add up the minumums
        minimum_total_cost += state_cost

    return minimum_total_cost
