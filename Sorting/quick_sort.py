def quick_sort(arr, low, high):
    if low < high:
        pivot = sorting(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def sorting(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] < p:
            i = i + 1
        while i <= j and arr[j] > p:
            j = j - 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j


items = [2, 9, 5, 3, 1, 7, 8, 4, 6]
last = len(items) - 1
quick_sort(items, 0, last)


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] > pivot:  # Compare for descending order
            left += 1
        while left <= right and arr[right] < pivot:  # Compare for descending order
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quick_sort_descending(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_descending(arr, low, pivot_index - 1)
        quick_sort_descending(arr, pivot_index + 1, high)

items = [2, 9, 5, 3, 1, 7, 8, 4, 6]
last = len(items) - 1
quick_sort_descending(items, 0, last)
print(items)
