from random import randint
import matplotlib.pyplot as plt
import math
import itertools




def less_than(a,b):
    global comparison_counter
    comparison_counter+=1
    return a<b
    """is_less_than = input("Is {} less than {}?\n".format(a,b))
    if is_less_than.lower() in ["true", "t", "yes", "y"]:
        return True
    elif is_less_than.lower() in ["false", "f", "no", "n"]:
        return False
    else:
        return less_than(a,b)"""

def less_than_equal(a,b):
    global comparison_counter
    comparison_counter+=1
    return a<=b
    """is_less_than = input("Is {} less than or equal to {}?\n".format(a,b))
    if is_less_than.lower() in ["true", "t", "yes", "y"]:
        return True
    elif is_less_than.lower() in ["false", "f", "no", "n"]:
        return False
    else:
        return less_than(a,b)"""


def bubble_sort_resumes(resume_list):
    n = len(resume_list)
    for i in range(n):
        for j in range(n-i-1):
            if user_decides_if_the_first_resume_is_better(resume_list[j], resume_list[j+1]):
                resume_list[j], resume_list[j+1] = resume_list[j+1], resume_list[j]

def user_decides_if_the_first_resume_is_better(resume1, resume2):
    a = input("Which is better, {} or {}?\n".format(resume1, resume2))
    if a.lower() == resume1.lower() or a==1:
        return True
    elif a.lower()==resume2.lower() or a==2:
        return False
    else:
        print("Error")
    # todo: implement me
    # return True if resume1 is better, False if resume2 is better


resume_list = ["c", "b", "d", "a"]
#bubble_sort_resumes(resume_list)





###############################################





def merge_insertion_sort(collection: list[int]) -> list[int]:
    global comparison_counter
    comparison_counter = 0
    def binary_search_insertion(sorted_list, item):
        left = 0
        right = len(sorted_list) - 1
        while less_than_equal(left, right):
            middle = (left + right) // 2
            if left == right:
                if less_than(sorted_list[middle], item):
                    left = middle + 1
                break
            elif less_than(sorted_list[middle], item):
                left = middle + 1
            else:
                right = middle - 1
        sorted_list.insert(left, item)
        return sorted_list

    def sortlist_2d(list_2d):
        def merge(left, right):
            result = []
            while left and right:
                if less_than(left[0][0], right[0][0]):
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            return result + left + right

        length = len(list_2d)
        if length <= 1:
            return list_2d
        middle = length // 2
        return merge(sortlist_2d(list_2d[:middle]), sortlist_2d(list_2d[middle:]))

    if len(collection) <= 1:
        return collection

    """
    Group the items into two pairs, and leave one element if there is a last odd item.
    Example: [999, 100, 75, 40, 10000]
                -> [999, 100], [75, 40]. Leave 10000.
    """
    two_paired_list = []
    has_last_odd_item = False
    for i in range(0, len(collection), 2):
        if i == len(collection) - 1:
            has_last_odd_item = True
        else:
            """
            Sort two-pairs in each groups.
            Example: [999, 100], [75, 40]
                        -> [100, 999], [40, 75]
            """
            if less_than(collection[i], collection[i + 1]):
                two_paired_list.append([collection[i], collection[i + 1]])
            else:
                two_paired_list.append([collection[i + 1], collection[i]])

    """
    Sort two_paired_list.
    Example: [100, 999], [40, 75]
                -> [40, 75], [100, 999]
    """
    sorted_list_2d = sortlist_2d(two_paired_list)

    """
    40 < 100 is sure because it has already been sorted.
    Generate the sorted_list of them so that you can avoid unnecessary comparison.
    Example:
           group0 group1
           40     100
           75     999
        ->
           group0 group1
           [40,   100]
           75     999
    """
    result = [i[0] for i in sorted_list_2d]

    """
    100 < 999 is sure because it has already been sorted.
    Put 999 in last of the sorted_list so that you can avoid unnecessary comparison.
    Example:
           group0 group1
           [40,   100]
           75     999
        ->
           group0 group1
           [40,   100,   999]
           75
    """
    result.append(sorted_list_2d[-1][1])

    """
    Insert the last odd item left if there is.
    Example:
           group0 group1
           [40,   100,   999]
           75
        ->
           group0 group1
           [40,   100,   999,   10000]
           75
    """
    if has_last_odd_item:
        pivot = collection[-1]
        result = binary_search_insertion(result, pivot)

    """
    Insert the remaining items.
    In this case, 40 < 75 is sure because it has already been sorted.
    Therefore, you only need to insert 75 into [100, 999, 10000],
    so that you can avoid unnecessary comparison.
    Example:
           group0 group1
           [40,   100,   999,   10000]
            ^ You don't need to compare with this as 40 < 75 is already sure.
           75
        ->
           [40,   75,    100,   999,   10000]
    """
    is_last_odd_item_inserted_before_this_index = False
    for i in range(len(sorted_list_2d) - 1):
        if result[i] == collection[-i]:
            is_last_odd_item_inserted_before_this_index = True
        pivot = sorted_list_2d[i][1]
        # If last_odd_item is inserted before the item's index,
        # you should forward index one more.
        if is_last_odd_item_inserted_before_this_index:
            result = result[: i + 2] + binary_search_insertion(result[i + 2 :], pivot)
        else:
            result = result[: i + 1] + binary_search_insertion(result[i + 1 :], pivot)

    #return result


nums = [4, 3, 5, 1, 2]
#print("\nOriginal list:")
#print(nums)
#print("After applying Merge-insertion Sort the said list becomes:")
#print(merge_insertion_sort(nums))

##################################################################
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

counter = 0
def count(x,y):
    global counter
    counter += 1
    return x < y

worsts = []
for m in range(9):
    print(m)
    worst = 0
    for perm in itertools.permutations(range(m)):
        counter = 0
        assert list(merge_insertion(perm, less=count)) == list(range(m))
        worst = max(worst, counter)
    worsts.append(worst)
print(worsts) # yields [0, 0, 1, 3, 5, 7, 10, 13, 16]

##################################################################



counter_ = 0

worsts_ = []
for m in range(9):
    print(m)
    worst = 0
    for perm in itertools.permutations(range(m)):
        comparison_counter = 0
        #print(perm)
        merge_insertion_sort(perm)
        if comparison_counter>worst:
            worst = comparison_counter
    worsts_.append(worst)
print(worsts_) # yields [0, 0, 1, 3, 5, 7, 10, 13, 16]







list_len = []
comparisons = []
for i in range(1000):
    ll = randint(0,50)
    list_len.append(ll)
    n = []
    for e in range(ll):
        n.append(randint(0,100))
    merge_insertion_sort(n)
    comparisons.append(comparison_counter)
xs = [i for i in range(1,100)]
ys = [i*math.log2(i)-1.41*i for i in xs]
yt = [(n*(math.log2(3*n/4)) - (2*(math.log2(6*n))/3) + (math.log2(6*n)/2)) for n in xs]
c = [0, 1, 3, 5, 7, 10, 13, 16, 19, 22, 26, 30, 34]
x = [1,2,3,4,5,6,7,8,9,10,11,12,13]
plt.plot(x,c, label="wiki theoretical max listed")
plt.plot(xs,ys,label="wiki theoretical max aprox")
plt.plot(xs, yt, label="wiki theoretical exact")
plt.scatter(list_len, comparisons, label="recorded data algo1")
plt.plot(worsts, label="worst recorded data algo2")
plt.plot(worsts_, label="worst recorded data algo1")
plt.legend()
plt.show()
