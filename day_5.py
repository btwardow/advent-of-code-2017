
# Day 5

# Task 1 - jumping...


def number_of_steps(b):
    i = 0
    s = 0
    while i >= 0 and i < len(b):
        j = b[i]  # get relative jump
        b[i] += 1  # increment
        i += j  # and jump
        s += 1
    return s


def parse(s):
    return list(map(int, s.split()))


# Task 1 - tests

s = '''
0
3
0
1
-3
'''

assert parse(s) == [0, 3, 0, 1, -3]
assert number_of_steps(parse(s)) == 5


# Task 2 -
def number_of_steps_with_decreasing(b):
    i = 0
    s = 0
    while i >= 0 and i < len(b):
        j = b[i]  # get relative jump
        if j >= 3:
            b[i] -= 1  #
        else:
            b[i] += 1  # increment
        i += j  # and jump
        s += 1
    return s


assert number_of_steps_with_decreasing(parse(s)) == 10
