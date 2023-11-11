from __future__ import print_function
import itertools

def binary_insert(seq, x, less):
    possible_positions = range(len(seq) + 1)
    L, R = 0, possible_positions[-1]
    while len(possible_positions) > 1:
        m = (L + R)//2
        if less(x, seq[m]):
            R = m
        else:
            L = m+1
        possible_positions = [p for p in possible_positions if L <= p <= R]
    return possible_positions[0]

def merge_insertion(seq, less):
    if len(seq) <= 1:
        return seq
    pairs = []
    for x1, x2 in zip(seq[::2], seq[1::2]):
        if less(x1, x2):
            pairs.append((x1, x2))
        else:
            pairs.append((x2, x1))
    # sort pairs by their large element
    pairs = merge_insertion(pairs, less=lambda a,b : less(a[1], b[1]))
    out = [x2 for x1, x2 in pairs]
    remaining = pairs[:]
    if len(seq) % 2 == 1:
        remaining.append((seq[-1], "END"))
    out.insert(0, remaining.pop(0)[0])
    # reorder remaining
    buckets = [2, 2]
    power_of_2 = 4
    while sum(buckets) < len(remaining):
        power_of_2 *= 2
        buckets.append(power_of_2 - buckets[-1])
    reordered = []
    last_index = 0
    for bucket in buckets:
        reordered += reversed(remaining[last_index:last_index+bucket])
        last_index += bucket
    for y, x in reordered:
        if x == "END":
            # insert unpaired element
            out.insert(binary_insert(out, y, less), y)
        else:
            # insert y in out by binary search up to but not including out.index(x)
            out.insert(binary_insert(out[:out.index(x)], y, less), y)
    return out



# test by calculating worst-case number of comparisons
if __name__ == "__main__":
    counter = 0
    counter = 0
    def count(x,y):
        global counter
        counter += 1
        return x<y

    worsts = []
    for m in range(10):
        print(m)
        worst = 0
        for perm in itertools.permutations(range(m)):
            counter = 0
            assert list(merge_insertion(perm, less=count)) == list(range(m))
            worst = max(worst, counter)
        worsts.append(worst)
    print(worsts) # yields [0, 0, 1, 3, 5, 7, 10, 13, 16]"""


