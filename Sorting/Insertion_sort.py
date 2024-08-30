"""
How it works:
Take the first value from the unsorted part of the array.
Move the value into the correct place in the sorted part of the array.
Go through the unsorted part of the array again as many times as there are values.
"""

"""
Question =1 

You have been given an A array consisting of N integers. All the elements in this array are guaranteed to be unique.
For each position i in the array A you need to find the position  should be present in,
if the array was a sorted array. You need to find this for each i and print the resulting solution.
"""


def insertion_sort(items):
    n = len(items)
    for i in range(1, n):
        temp = i
        current_value = items.pop(i)
        for j in range(i - 1, -1, -1):
            if items[j] > current_value:
                temp = current_value
        items.insert(temp, current_value)
    return items


print(insertion_sort([8, 45, 233, 5, 2, 4, 5, 34, 34, 23, 45, 54, ]))

# Example = 1
"""
def insertion_method(arr):
    n = len(arr)
    for i in range(1, n):  # [2, 5, 3, 11, 9, 4, 7]
        temp = arr[i]
        j = i - 1
        for j in range(i - 1, -1, -1):
            if temp < arr[j]:
                arr[j + 1] = arr[j]
            else:
                break
        arr[j+1] = temp

    return arr


items = [2, 5, 3, 11, 9, 4, 7]
print(insertion_method(items)),
"""


# Example 2

my_array = [64, 34, 25, 12, 22, 11, 90, 5]






n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_value

print("Sorted array:", my_array)
