# Day 7

# Task 1
def parse_line(l):
    ls = l.split()
    n = ls[0]
    w = int(ls[1][1:-1])
    a = []
    if len(ls) > 2:
        a = [s.strip() for s in l.split('->')[1].split(',')]
    return (n, w, a)

def read_graph(s):
    g = dict()
    for l in s.splitlines():
        if l.strip():
            (r_n, r_w, r_a) = parse_line(l)
            g[r_n] = (r_w, r_a)
    return g

def root(g):
    having_parents = set()
    for k, (w, a) in g.items():
        if a:
            having_parents |= set(a)
    # only root should have no parent
    roots = g.keys() - having_parents
    assert len(roots) == 1
    return roots.pop()

# Task 1  - Tests
assert parse_line("bdafpm (58)") == ('bdafpm', 58, [])

l = "rmlddp (64) -> rufvv, gxiwcqv, cjcapa, exwxepj, qvbfob, zimrsr, nrcbij"
expected_r_n = 'rmlddp'
expected_r_w = 64
expected_r_a = 'rufvv,gxiwcqv,cjcapa,exwxepj,qvbfob,zimrsr,nrcbij'.split(',')
(r_n, r_w, r_a) = parse_line(l)
assert r_n == expected_r_n
assert r_w == expected_r_w
assert r_a == expected_r_a

t = '''
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
'''
assert root(read_graph(t)) == 'tknk'

# Task 2 - Find unbalanced nodea
import sys
def balance(g, r):
    _cache = dict()
    def _get_node_weight(n): #recurrence with memoriztion
        if n not in _cache:
            (w, childs) = g[n]
            _cache[n] = w + sum(_get_node_weight(c) for c in childs) if childs else w
        return _cache[n]

    (w, childs) = g[r]
    if not childs: return sys.maxsize
    childs_weights = [_get_node_weight(c) for c in childs]
    # what is mode?
    from collections import Counter
    mode = Counter(childs_weights).most_common(1)[0][0]
    to_balance = None
    for c, w in zip(childs, childs_weights):
        if w != mode:
            to_balance = g[c][0] + ( mode - w)
    if to_balance:
       return min(to_balance, *(balance(g, c) for c in childs))
    else:
       return min(balance(g, c) for c in childs)


g = read_graph(t)
assert balance(g, root(g)) == 60
