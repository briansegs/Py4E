"""Regex assignment"""
import re

# Example sum == 445833
# handler = open('regex_sum_42.txt')

handler = open('regex_sum_1919206.txt')
total = 0
for line in handler:
    nums = re.findall('[0-9]+', line)
    if nums == []:
        continue
    for num in nums:
        total += int(num)
print(total)
