def find_ceo(num_employees):
    ceo_experience = 0
    experience_levels = num_employees.keys()
    experience_levels.sort(reverse = True)
    top_experience_level = experience_levels[0]

    current_level = experience_levels.pop()
    unmanaged_employees = num_employees[current_level]

    # construct graph from leaves and count unmanaged employees
    while len(experience_levels) > 0:
        manager_level = experience_levels.pop()
        manager_employees = num_employees[manager_level]
        unmanaged_employees -= min(manager_employees * manager_level, unmanaged_employees)
        unmanaged_employees += manager_employees
        # print("Level {}: {} unmanaged employees".format(manager_level, unmanaged_employees))
        current_level = manager_level

    ceo_experience = max(top_experience_level + 1, unmanaged_employees)
    return ceo_experience

def driver():
    t = int(raw_input())
    for i in range(1, t + 1):
        l = int(raw_input())
        employee_counts = dict()
        for x in range(l):
            n, e = [int(s) for s in raw_input().split(" ")]
            employee_counts[e] = n
        result = find_ceo(employee_counts)
        print("Case #{}: {}".format(i, result))

driver()
