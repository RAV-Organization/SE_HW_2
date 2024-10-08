"""Module providing a function for randomizing the elements in an array."""
import subprocess


def random_array(arr):
    """Function for randomizing an array input."""
    shuffled_num = None
    # for i in range(len(arr)):
    for i, _ in enumerate(arr):
        # shuffled_num = subprocess.run(
        #     ["shuf", "-i1-20", "-n1"], capture_output=True)
        # arr[i] = int(shuffled_num.stdout)
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
