# Day 12

# Task 1 - Digital Plumber


def dfs(g, v_start=0):
    '''
    Deep First Search for a given graph
    and return number of vertices in a
    connected component.abs

    Parameters
    ----------

    Returns
    -------
    int :
        Number of vertices.
    '''
    visited = [0] * len(g)
    def _dfs(v):
        if visited[v]: return
        else:
            visited[v] = 1
            for v2 in g[v]:
                _dfs(v2)

    _dfs(v_start)
    v_start_count = sum(visited)
    groups = 1
    while sum(visited) < len(visited):
        for i, v in enumerate(visited):
            if v == 0:
                _dfs(i)
                groups += 1
                break
    return (v_start_count, groups)


def _parse(s):
    '''
    s is ordered
    '''
    r = []
    for l in s.splitlines():
        if l.strip():
            v1, adj_csv = l.split(' <-> ')
            r.append([int(v2) for v2 in adj_csv.split(',')])
    return r

# Task 1 - Parse
g_input = '''
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
'''

g = _parse(g_input)
assert len(g) == 7
assert g[0] == [2]
assert g[1] == [1]

assert dfs(g)[0] == 6


# Task 2 - Number of groups
assert dfs(g)[1] == 2
