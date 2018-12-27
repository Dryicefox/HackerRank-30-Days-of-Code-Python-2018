### Name: Verneri Kalviainen (dryicefox)
### Date: 12/27/2018
### Title: Day 10: Binary Numbers
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    current_consecutive_1s = 0
    max_consecutive_1s = 0
    while(n > 0):
        remainder = n%2
        if remainder ==1:
            current_consecutive_1s += 1
            if current_consecutive_1s > max_consecutive_1s:
                max_consecutive_1s = current_consecutive_1s
        else:
            current_consecutive_1s = 0

        n = n // 2

    print(max_consecutive_1s)
