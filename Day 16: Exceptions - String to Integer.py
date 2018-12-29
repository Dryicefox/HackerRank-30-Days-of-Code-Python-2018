### Name: Verneri Kalviainen (dryicefox)
### Date: 12/28/2018
### Title: Day 15: Linked List
#!/bin/python3

import sys


S = input().strip()

try:
    integer_value = int(S)
    print(integer_value)
except ValueError:
    print('Bad String')
