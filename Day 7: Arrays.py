### Name: Verneri Kalviainen (dryicefox)
### Date: 12/26/2018
### Title: Day 7: Arrays

##Important note, works in compiler, but not on the website as of October, 1, 2018

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    reversed_array = []
    for i in range(n):
        reversed_array.append[arr[n-1-i]]

    for i in range(len(reversed_array)):
        output_string += str[reversed_array[i]] + ' '

    print(output_string)

