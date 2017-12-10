# Day 10

# Task 1

def hash(length_seq, n = 256):
    a = list(range(n))
    i = 0
    skip = 0
    for l in length_seq:
        #reverse
        s = i
        e = i + l - 1
        while s < e:
            tmp = a[s %n]
            a[s %n] = a[e %n]
            a[e %n] = tmp
            s += 1
            e -= 1
        i += (l + skip) %n
        skip += 1
    return a[0] * a[1], a

# Task 1 - Tests
assert hash([3, 4, 1, 5], 5)[0] == 12

# Task 2
def hash2(s):
    n = 256
    # ASCII to int + suffix
    seq = ([ord(c) for c in s] + [17, 31, 73, 47, 23] ) * 64
    # 64 x hashing
    hash1, a = hash(seq, n)
    # XOR-ing
    r = []
    for i in range(16):
        x = a[i * 16 ]
        for j in range(1, 16):
            x ^= a[i * 16 + j ]
        r.append(x)
    # to hexadecimal
    return ''.join([ hex(i)[2:].zfill(2) for i in r])


# Taks 2 - Tests
assert hash2('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert hash2('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert hash2('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert hash2('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

