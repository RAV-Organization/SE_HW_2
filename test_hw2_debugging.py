from hw2_debugging import merge_sort
from rand import random_array


def test_case1():
    ARR = random_array([0] * 20)
    arr_out = merge_sort(ARR)
    assert arr_out == sorted(ARR)
    # print(arr_out)
    # print(sorted(ARR))

