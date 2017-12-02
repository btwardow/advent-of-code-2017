
# Task 1 - Checking the spreadsheet
def spreadsheet_checksum(m):
    int_m = [ [ int(c) for c in r.split() ] for r in m.splitlines() if r.strip()]
    return sum (  max(r) - min(r)  for r in int_m )


# Task 1 - Tests
t = '''
5 1 9 5
7 5 3
2 4 6 8
'''

assert spreadsheet_checksum(t) == 18


# Task 2 - evenly divisible values
def sum_evenly_divisible(m_str):
    m = [ [ int(c) for c in r.split() ] for r in m_str.splitlines() if r.strip()]
    s = 0
    for r in m:
        for i in range(len(r) - 1):
            for j in range(i + 1, len(r)):
                a, b = (r[i], r[j]) if r[i] > r[j] else (r[j], r[i])
                if a % b == 0:
                    s += a // b
    return s

# Task 2 - Tests
m = '''
5 9 2 8
9 4 7 3
3 8 6 5
'''

assert sum_evenly_divisible(m) == 9


