### Name: Verneri Kalviainen (dryicefox)
### Date: 12/27/2018
### Title: Day 7: Arrays

##!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr2 = arr.copy() # If we set arr2 to arr then all we have is a pointer, not a new list
    strvar = ''

    arr_length = len(arr) # 4 in this case, used for readability

    for i in range(arr_length):
        #Take the array and go backwards to copy backwards
        arr2[arr_length-1-i] = arr[i]

    for i in range(arr_length):
        strvar += (str(arr2[i]) + ' ')
    print(strvar)
