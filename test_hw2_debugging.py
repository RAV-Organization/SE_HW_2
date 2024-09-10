# """Module providing a function printing python version."""
from hw2_debugging import merge_sort
from rand import random_array


def test_case1():
    """Function printing python version."""
    arr_example_1 = random_array([0] * 20)
    arr_out = merge_sort(arr_example_1)
    assert arr_out == sorted(arr_example_1)
    # print(arr_out)
    # print(sorted(ARR))


def test_case2():
    """Function printing python version."""
    arr_example_2 = [10,9,9,5,3,1,2,47]
    arr_out = merge_sort(arr_example_2)
    assert arr_out == sorted(arr_example_2)
    # print(arr_out)
    # print(sorted(ARR))

def test_case3():
    """Function printing python version."""
    arr_example_3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    arr_out = merge_sort(arr_example_3)
    assert arr_out == sorted(arr_example_3)
    # print(arr_out)
    # print(sorted(ARR))