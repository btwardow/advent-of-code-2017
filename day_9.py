# Day 9

# Task 1 - Stream Processing
def groups_score(s):
    n = len(s)
    i = 0
    stack = []
    result = 0
    g_count = 0
    while i < n:
        c = s[i]
        if c == '!': # escape char
            i += 2
            continue
        if c == '<': # garbage start
            i += 1
            while i < n:
                c = s[i]
                if c == '!': # escape char
                    i += 2
                    continue
                if c == '>':
                    break
                i += 1 # eat it
                g_count += 1
        if c == '{': # group start
            score = 1 if len(stack) == 0 else (stack[-1] + 1)
            stack.append(score)
        if c == '}': # group end
            result += stack.pop()
        # move alonge
        i += 1
    return result, g_count


assert groups_score('{}') == (1, 0)
assert groups_score('{{{}}}') == (6, 0)
assert groups_score('{{},{}}') == (5, 0)
assert groups_score('{{{},{},{{}}}}') == (16, 0)
assert groups_score('{<a>,<a>,<a>,<a>}') == (1, 4)
assert groups_score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == (9, 8)
assert groups_score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == (9, 0)
assert groups_score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == (3, 17)

