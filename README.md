# Manual-Sort
Manually compare and sort items using Insertion Sort algorithm


"Ranked Comparison between things.py" assesses how two different sorting algorithms compare to each other based on the maximum number of comparisons needed to sort a list of length n. These are plotted agains n for comparison. It also plots the wikipedia theoretical maximum number of comparisons between elements for a merge-insertion sort (https://en.wikipedia.org/wiki/Merge-insertion_sort#:~:text=giving%20the%20formula,the%20OEIS).


"Best ranked comparison between things.py" actually allows the user to test the algorithm which was found to be most efficient in terms of minimising the maximum number of comparisons needed to sort any lsit. 
Start by inputting comma separated values (numerical or strings non "" needed)

The program will ask for comparisons between values which can be answered with y/n ... i.e. "is z less than b?" which would be "n" for an alphabetically sorted list

Use case is for ordering lists based on qualitative manual comparisons. i.e. sorting CVs into order from worst to best.

Merge-insertion sort is the sorting algorithm with the minimum possible comparisons for n n items whenever n ≤ 22, and it has the fewest comparisons known for n ≤ 46. - https://en.wikipedia.org/wiki/Merge-insertion_sort#:~:text=Merge%2Dinsertion%20sort%20is,fewest%20comparisons%20known%20for
