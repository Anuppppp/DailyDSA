"""
Given an array arr[] consisting of N integers, the task is to sort the given array by using Bubble Sort without using loops.
"""
nums = [1, 56, 2, 3, 4, 33, 10, 11, 12, 8, 7, 33, 23, 5, 3423, 67, 897, 6543, 23]
n = len(nums)
for i in range(n):
    for j in range(0, n - i - 1):
        # Swap if the element found is greater
        # than the next element
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)

"""
Given an array arr[] consisting of N integers, the task is to sort the given array by using Bubble Sort without using loops.

Examples:

Input: arr[] = {1, 3, 4, 2, 5}
Output: 1 2 3 4 5

Input: arr[] = {1, 3, 4, 2}
Output: 1 2 3 4
"""
arr = [6, 1, 7, 4, 2, 5]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)


"""
Q2. Write a program to arrange all alphabets of “csiplearninghub” into descending order using bubble sort.
"""
alpha = list("csiplearninghub")
n = len(alpha)
for i in range(n-1):
    for j in range(0, n-i-1):
        if alpha[j] > alpha[j+1]:
            alpha[j], alpha[j + 1] = alpha[j+1], alpha[j]

print(alpha)

"""
Q3. Write a program to accept five names from user and arrange in increasing order using bubble sort.
"""
n = 5
items = []
while n > 0:
    user = int(input("Enter a number: ", ))
    items.append(user)
    n = n - 1

print(items)
num = len(items)
for i in range(num):
    for j in range(0, num - i - 1):
        if items[j+1] > items[j]:
            items[j+1], items[j] = items[j], items[j+1]
print(items)

"""
Q4. Write a program to accept numbers from the user till the user enter ZERO and store them in a list.
 After that arrange them in increasing order using bubble sort.
"""
zero = True
items = []
while zero:
    user = int(input("Insert a number : ", ))
    items.append(user)
    if user == 0:
        items.pop(-1)
        zero = False
print(items)


"""
Given an array nums with n objects colored red, white, or blue,sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.We will use the integers 0, 1, and 2 to represent
the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""



def sort_colors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


"""

"""

def two_sum(numbers, target):
    n = len(numbers)
    # print(obj)
    for i in range(n):
        second = target - numbers[i]
        if second in numbers:
            return second, numbers[i]


nums = [2, 7, 19, 11]
res = two_sum(nums, 9)
print(res)

