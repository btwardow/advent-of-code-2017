# Day 11

# Task 1 - hex ed

def hex_dist(moves):
    '''
    Calculate final distance in the hex-grid for a
    given moves list. For a reading see this:
        https://www.redblobgames.com/grids/hexagons/#coordinates-offset

    Parameters
    ----------
    moves: list
        List of moves as a CSV string.

    Returns
    -------
    int
        Distance in hexagonal grid space.

    '''

    class Cube:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    cube_directions = {
        'se': Cube(+1, -1,  0),
        'ne': Cube(+1,  0, -1),
        'n' : Cube( 0, +1, -1),
        'nw': Cube(-1, +1,  0),
        'sw': Cube(-1,  0, +1),
        's' : Cube( 0, -1, +1)
    }

    def _cube_dist(a, b):
        return (abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) // 2

    start = Cube(0,0,0)
    end = Cube(0,0,0)
    max_dist = 0
    for m in moves.split(','):
        d = cube_directions[m]
        end.x += d.x
        end.y += d.y
        end.z += d.z
        max_dist = max(max_dist, _cube_dist(start, end))

    return _cube_dist(start, end), max_dist



# Task 1 - Tests
assert hex_dist('ne,ne,ne')[0] == 3
assert hex_dist('ne,ne,sw,sw')[0] == 0
assert hex_dist('ne,ne,s,s')[0] == 2
assert hex_dist('se,sw,se,sw,sw')[0] == 3


# Task 2 - adding max
