"""Module providing a function to perform merge sort on an array."""
from rand import random_array


def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return recombine(left, right)


def recombine(left_arr, right_arr):
    """Merges two sorted arrays into one sorted array."""
    left_index, right_index = 0, 0
    merge_arr = []

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # Add remaining elements from both arrays
    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])

    return merge_arr


# Example usage
ARR = random_array([0] * 20)
arr_out = merge_sort(ARR)
print(arr_out)
