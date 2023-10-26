"""Assignment 8.5"""

# Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# You will parse the From line using split() and print out the second
# word in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.

file = input("Enter file name: ")
file_handler = open(file)

count = 0
for line in file_handler:
    if line.startswith("From "):
        lst = line.split(" ")
        print(lst[1])
        count += 1
print(f"There were {count} lines in the file with From as the first word")
