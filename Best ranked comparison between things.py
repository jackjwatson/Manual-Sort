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

counter = 0
def count_man(x,y):
        global counter
        counter += 1
        is_less_than = input("Is {} less than {}?\n".format(x,y))
        if is_less_than.lower() in ["true", "t", "yes", "y"]:
            return True
        elif is_less_than.lower() in ["false", "f", "no", "n"]:
            return False
        else:
            return less_than(a,b)
def count(x,y):
        global counter
        counter += 1
        return x<y



unsorted_list = input("Please input your comma separated list of items:\n")
unsorted_list = unsorted_list.split(",")
worst=0
for perm in itertools.permutations(range(len(unsorted_list))):
    counter = 0
    assert list(merge_insertion(perm, less=count)) == list(range(len(unsorted_list)))
    worst = max(worst, counter)
counter=0
print(merge_insertion(unsorted_list, count_man))
print("calculated with {} comparisons of a maximum of {} for a list of {} items!".format(counter, worst, len(unsorted_list)))
