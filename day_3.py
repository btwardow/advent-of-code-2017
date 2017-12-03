# Day 3

# Task 1 - Spiral Memory
def spiral_coord(n):
    # radius of spiral
    r = 0
    # center of spiral
    yield 0,0
    # start spinning...
    while n > 0:
        # start new spiral
        r += 1
        # up
        for dy in range(r - 1, -r, -1):
            n -= 1
            if n > 0:  yield r, dy
        # left
        for dx in range(r, -r, -1):
            n -= 1
            if n > 0: yield dx, -r
        # down
        for dy in range(-r, r):
            n -= 1
            if n > 0: yield -r, dy
        # right
        for dx in range(-r, r + 1):
            n -= 1
            if n > 0: yield dx, r

def manhattan_dist_in_spiral(n):
    dx, dy = list(spiral_coord(n))[-1]
    return (dx if dx > 0 else -dx) + (dy if dy > 0 else -dy)

assert manhattan_dist_in_spiral(8) == 1
assert manhattan_dist_in_spiral(23) == 2
assert manhattan_dist_in_spiral(289326) == 419


# Task 2 - Spiral with adjacent sums
MASK = list(spiral_coord(9))
def next_value_after(v):
    s = {(0,0): 1}
    for x, y in spiral_coord(9999999):
        neigbours_sum = sum([s.get((x + dx, y + dy), 0) for (dx, dy) in MASK])
        if neigbours_sum > v:
            return neigbours_sum
        s[x,y] = neigbours_sum


assert next_value_after(5) == 10
assert next_value_after(351) == 362
