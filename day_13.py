# Day 13


# Task 1


def _parse(s):
    s = s.strip()
    p = [(int(v1), int(v2))
         for v1, v2 in [l.split(': ') for l in s.splitlines()]]
    layers_n = p[-1][0] + 1
    r = [-1] * layers_n
    for i, v in p:
        r[i] = v
    return r


def collisions(f, start_step=0):
    n = len(f)
    collisions = []
    for step in range(n):  # moves the packege forward through layers
        picosecond = start_step + step
        # check collision
        # calculate scanner at step position
        x = f[step] - 1
        scanner = x - abs((picosecond) % (2 * x) - x)
        if scanner == 0:
            collisions.append(picosecond)
    return collisions


def severity(f, c):
    return sum(_c * f[_c] for _c in c)

# Task 1 - Tests


s = '''
0: 3
1: 2
4: 4
6: 4
'''

f = _parse(s)
assert len(f) == 7
assert f[1] == 2

c = collisions(f)
assert c == [0, 6]
assert severity(f, c) == 0*3 + 6*4


# Task 2 - Pass throught without collision

def delay_for_pass(f, max_delay=9999999):
    for i in range(max_delay):
        if len(collisions(f, i)) == 0:
            return i


assert delay_for_pass(f) == 10
