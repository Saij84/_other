# x = [
#     [1, 1, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0],
#     [0, 0, 2, 4, 4, 0],
#     [0, 0, 0, 2, 0, 0],
#     [0, 0, 1, 2, 4, 0]]


x = [
    [3, 7, -3, 0, 1, 8],
    [1, -4, -7, -8, -6, 5],
    [-8, 1, 3, 3, 5, 7],
    [-2, 4, 3, 1, 2, 7],
    [2, 4, -5, 1, 8, 4],
    [5, -7, 6, 5, 2, 8]]

#!/bin/python3

import math
import os
import random
import re
import sys


def construct_arr(arr):
    """

    :param arr: 6x6 array
    :return: int -> max value
    """
    idx_remove = [3, 5]
    return_arr = []
    transient_arr = [[], [], [], []]

    for y in range(4):
        for sub_arr in enumerate(arr[y: y+3]):
            for x in range(4):
                transient_arr[x].extend(sub_arr[1][x: x+3])
        return_arr.extend([sum([i[1] for i in enumerate(sum_arr) if not i[0] in idx_remove]) for sum_arr in transient_arr])
        transient_arr = [[], [], [], []]
    return max(return_arr)



if __name__ == '__main__':
    arr = x

    # for _ in range(6):
    #     data_in = x #input()
    #     arr.append(list(map(int, data_in.rstrip().split())))

    print(construct_arr(arr))


