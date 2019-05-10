#!/bin/python3
from utils.src.array_utils import array_utils as aUtils
from utils.src.time_utils import time_utils as tUtils


import sys

n = [3, 2, 1] #aUtils.array_generator(0, 600, arr_size=600)
# Write Your Code Here

swaps = 0
current_num = 0

@tUtils.function_timer
def do_it(a):
    arr_len = len(a)-1
    count = 0
    sort_arr = []
    for rep in range(arr_len):
        for i in range(arr_len):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                count += 1
    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
do_it(n)
