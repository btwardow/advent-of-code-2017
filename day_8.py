# Day 8

# Task 1 - What is the largest value in any register?

def compute(symbols, ops):
    # initialize registers
    r = dict()
    max_val = - 2**32
    for s in symbols: exec('{} = 0'.format(s), globals(), r)
    # compute conditionaly
    for con, op in ops:
        if eval(con, globals(), r):
            exec(op, globals(), r)
            max_val = max(max_val, eval(op.split()[0], globals(), r))
    return r, max_val

def larget_register_value(r):
    return max(r.values())

def parse(s):
    '''
    Returns all registers and list of (condition, operation) touples
    which can be evaluated by python.
    '''
    reg = set()
    inst = []
    for l in s.splitlines():
        l = l.strip()
        if l:
            op, con = l.split('if')
            s_op = op.split()
            s_con = con.split()
            reg.add('_' + s_op[0])
            reg.add('_' + s_con[0])
            op = op.replace('inc', '+=')
            op = op.replace('dec', '-=')
            inst.append(( '_' + con.strip(), '_' + op.strip()))
    return reg, inst


# Task  1 - Tests

t = '''
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''

i = parse('hwv inc 149 if clj >= -5')
expected_reg = {'_clj', '_hwv'}
expected_inst = ('_clj >= -5', '_hwv += 149')
assert i[0] == expected_reg
assert i[1][0] == expected_inst

reg, ops = parse(t)
r, max_val = compute(reg, ops)
assert larget_register_value(r) == 1

# Task 2 - Max val
# added in prepared script
assert max_val == 10
