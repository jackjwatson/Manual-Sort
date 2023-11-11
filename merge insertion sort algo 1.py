def less_than(a,b):
    is_less_than = input("Is {} less than {}?\n".format(a,b))
    if is_less_than.lower() in ["true", "t", "yes", "y"]:
        return True
    elif is_less_than.lower() in ["false", "f", "no", "n"]:
        return False
    else:
        return less_than(a,b)

def less_than_equal(a,b):
    is_less_than = input("Is {} less than or equal to (e) {}?\n".format(a,b))
    if is_less_than.lower() in ["true", "t", "yes", "y"]:
        return True
    elif is_less_than.lower() in ["false", "f", "no", "n"]:
        return False
    else:
        return less_than(a,b)


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

    def binary_search_insertion(sorted_list, item):
        left = 0
        right = len(sorted_list) - 1
        while left <= right:
            middle = (left + right) // 2
            if left == right:
                if sorted_list[middle] < item:
                    left = middle + 1
                break
            elif sorted_list[middle] < item:
                left = middle + 1
            else:
                right = middle - 1
        sorted_list.insert(left, item)
        return sorted_list

    def sortlist_2d(list_2d):
        def merge(left, right):
            result = []
            while left and right:
                if left[0][0] < right[0][0]:
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
            if collection[i] < collection[i + 1]:
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

    return result


nums = [4, 3, 5, 1, 2]
print("\nOriginal list:")
print(nums)
print("After applying Merge-insertion Sort the said list becomes:")
print(merge_insertion_sort(nums))

