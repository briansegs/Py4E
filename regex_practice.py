""""Regex practice"""
import re

x = "my 2 favorite numbers are 19 and 42"
q = "From: Using the : character"
z = "From stephen.marquard@uct.ac.za. Sat Jan 5 09:14:16 2008"
# y = re.findall('[0-9]+', x)
# y = re.findall('^F.+?:', q)
# y = re.findall('\S+@\S+', z)
# y = re.findall('^From (\S+@\S+)', z)
# y = re.findall('@([^ ]*)', z)
# y = re.findall('^From .*@([^ ]*)', z)
# print(y)

handler = open('mbox-short.txt')
num_list = list()
for line in handler:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    num_list.append(num)
print('Maximum:', max(num_list))
