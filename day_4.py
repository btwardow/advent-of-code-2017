# Day 4

# Task 1 - Password veryfication


def number_of_valid(passwords):
    l = [l for l in passwords.splitlines() if l.strip()]
    n = 0
    for p in l:
        w = p.split()
        if len(set(w)) == len(w):
            n += 1
    return n

passwords = '''
aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa
'''

# Task 1 - Tests

assert number_of_valid(passwords) == 2

# Task 2 - Passwords without anagrams

def number_of_valid_without_anagrams(passwords):
    l = [l for l in passwords.splitlines() if l.strip()]
    n = 0
    for p in l:
        w = p.split()
        a = set(''.join(sorted(w_)) for w_ in w)
        if len(a) == len(w):
            n += 1
    return n

# Task 2 - Tests

assert number_of_valid_without_anagrams('abcde fghij') == 1
assert number_of_valid_without_anagrams('abcde xyz ecdab') == 0
assert number_of_valid_without_anagrams('a ab abc abd abf abj') == 1
assert number_of_valid_without_anagrams('iiii oiii ooii oooi oooo') == 1
assert number_of_valid_without_anagrams('oiii ioii iioi iiio') == 0


passwords = '''
abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio
'''

assert number_of_valid_without_anagrams(passwords) == 3
