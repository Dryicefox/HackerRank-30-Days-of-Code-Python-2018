### Name: Verneri Kalviainen (dryicefox)
### Date: 12/26/2018
### Title: Day 4: Class vs. Instance
num_test_cases = int(input())

for i in range(num_test_cases):
        test_string = input()
        even_indexed_characters = ''
        odd_indexed_characters = ''

        for j in range(len(test_string)):
            if j % 2 == 0:
                even_indexed_characters += test_string[j]
            else:
                odd_indexed_characters += test_string[j]

        print('{} {}'.format(even_indexed_characters, odd_indexed_characters))
