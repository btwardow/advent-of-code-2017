
# Day 1 - Task 1
def find_sum_of_repeted_digits(s):
    d = []
    for i in range(len(s)):
        if s[i] == s[i-1]:
            d.append(int(s[i]))
    return sum(d)


# tests
assert find_sum_of_repeted_digits('1122') == 3
assert find_sum_of_repeted_digits('1111') == 4
assert find_sum_of_repeted_digits('1234') == 0
assert find_sum_of_repeted_digits('91212130') == 9


# Day 1 - Task 2
def find_sum_of_repeted_digits_in_half_way(s):
    n = len(s)
    assert n % 2 == 0
    d = []
    for i in range(n):
        if s[i] == s[( i + (n//2)) % n]:
            d.append(int(s[i]))
    return sum(d)


# tests
assert find_sum_of_repeted_digits_in_half_way('1212') == 6
assert find_sum_of_repeted_digits_in_half_way('1212') == 0
assert find_sum_of_repeted_digits_in_half_way('12131415') == 4
