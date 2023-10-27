"""Assignment 10.2"""

# Write a program to read through the mbox-short.txt and figure
# out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the
# time and then splitting the string a second time using a colon.

# "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

file = input("Enter the file name: ")
if len(file) <= 0:
    file = "mbox-short.txt"
file_handler = open(file)

hour_count = dict()
for line in file_handler:
    if line.startswith("From "):
        line_list = line.split(" ")
        hour = line_list[6][:2]
        hour_count[hour] = hour_count.get(hour, 0) + 1

sorted_hours = sorted([(h, c) for h, c in hour_count.items()])
for hour, count in sorted_hours:
    print(hour, count)
        