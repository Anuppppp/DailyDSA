#                                                  SELECTION SORTING                                                   #


"""
How it works:

Go through the array to find the lowest value.
Move the lowest value to the front of the unsorted part of the array.
Go through the array again as many times as there are values in the array.
"""

"""
Modify the Selection Sort algorithm to sort the array in ascending order instead of ascending order.
"""
from typing import Tuple


def selection_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i  # let suppose the first element is minimum value
        for j in range(i + 1, n):  # here we left the first element
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


items = [3, 5, 1, 6, 7]
sorted_items = selection_sort_asc(items)
print(sorted_items)


"""
Modify the Selection Sort algorithm to sort the array in descending order instead of ascending order.
"""


def selection_sort_dsc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


items = [2, 4, 6, 1]
print(selection_sort_dsc(items))


"""
Find k-th Smallest Element
Description: Use the selection sort algorithm to find the k-th smallest element in an unsorted array.
"""

def kth_smallest(arr: list, k: int) -> tuple[list, int]:
    n = len(arr)
    for i in range(n):
        min_value = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_value]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]
    return arr[k-1]


print(kth_smallest([7, 10, 4, 3, 20, 15], 3))  # Output: 7

"""
Sort an Array of Strings
Description: Modify the selection sort algorithm to sort an array of strings based on their lengths.
def selection_sort_strings(arr: list) -> list:
    pass
print(selection_sort_strings(["apple", "banana", "kiwi", "cherry"]))  # Output: ["kiwi", "apple", "cherry", "banana"]
"""

def selection_sort_strings(arr: list) -> list:
    n = len(arr)
    if n == 1:
        return arr
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if len(arr[j]) < len(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
print(selection_sort_strings(["apple", "banana", "kiwi", "cherry"]))
Output: ["kiwi", "apple", "cherry", "banana"]

"""
Write a function to count the number of swaps performed by the selection sort algorithm.

def count_swaps_selection_sort(arr: list) -> int:
    pass
print(count_swaps_selection_sort([64, 25, 12, 22, 11]))  # Output: 4
"""


def count_swaps_selection_sort(arr: list, count: int) -> tuple[list, int]:
    n = len(arr)
    if n == 1:
        return arr, count
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                count = count + 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, count


print(count_swaps_selection_sort([1, 2, 3, 11], 0))  # Output: 4

"""
Modify the Selection Sort algorithm to sort the array in descending order instead of ascending order.
"""


def selection_sort(items):
    n = len(items)
    idx = 0
    for i in range(n):
        idx = i # 0 = 1
        for j in range(i + 1, n):
            if items[j] < items[idx]:
                items[j], items[idx] = items[idx], items[j]
    return items


print(selection_sort([3, 1, 67, 45, 23, 213, 43, 34, 12, 64, 87, 22]))
