def convert(A):
    x = [s.split(" ") for s in A.splitlines()]

    return x

def register_execute(A):
    registers = {}
    max_value = 0

    for line in A:
        register = line[0]
        inc = line[1]
        amt = int(line[2])
        condition_register = line[4]
        condition = line[5]
        condition_value = int(line[6])

        if condition_register not in registers:
            registers[condition_register] = 0
        condition_register_value = registers[condition_register]

        if condition == '==':
            if condition_register_value != condition_value:
                continue
        elif condition == '!=':
            if condition_register_value == condition_value:
                continue
        elif condition == '<':
            if condition_register_value >= condition_value:
                continue
        elif condition == '<=':
            if condition_register_value > condition_value:
                continue
        elif condition == '>':
            if condition_register_value <= condition_value:
                continue
        elif condition == '>=':
            if condition_register_value < condition_value:
                continue

        if register not in registers:
            registers[register] = 0

        value = registers[register]
        if inc == "inc":
            value += amt
        elif inc == "dec":
            value -= amt
        registers[register] = value
        max_value = max(value, max_value)

    # v = registers.values()
    # #print(v)
    # max_value = max(v)

    return max_value
