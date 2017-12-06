# Day 6

# Task 1
def number_of_redistribution_cycles(s):
    b = list(map(int, s.split()))
    states = dict()
    t = 0 # clock ticks
    while tuple(b) not in states:
        # save the state as seen
        states[tuple(b)] = t
        # take the first most loaded block
        max_i = 0
        for i in range(1, len(b)):
            if b[i] > b[max_i]:
                max_i = i
        # take all this memory blocks and...
        m = b[max_i]
        b[max_i] = 0
        # ...redistriute
        for i in range(1, m + 1):
            b[(max_i + i) % len(b)] += 1
        t += 1

    return len(states), t - states[tuple(b)]

# Task 1 - Test
t = '0    2     7  0'
assert number_of_redistribution_cycles(t)[0] == 5

# Task 2 - Test
assert number_of_redistribution_cycles(t)[1] == 4
