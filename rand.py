"""Module providing a function printing python version."""
import subprocess

def random_array(arr):
    """Function printing python version."""
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True)
        arr[i] = int(shuffled_num.stdout)
    return arr


# import random


# def random_array(arr):
#     """Fills the array with random integers between 1 and 20."""
#     for i in range(len(arr)):
#         arr[i] = random.randint(1, 20)
#     return arr
