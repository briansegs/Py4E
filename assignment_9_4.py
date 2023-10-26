"""Assignment 9.5"""

# -Write a program to read through the mbox-short.txt and
#  figure out who has sent the greatest number of mail messages.
# -The program looks for 'From ' lines and takes the second word
#  of those lines as the person who sent the mail.
# -The program creates a Python dictionary that maps the sender's
#  mail address to a count of the number of times they appear in the file.
# -After the dictionary is produced, the program reads through the
#  dictionary using a maximum loop to find the most prolific committer.

file = input("Enter the file name: ")
if len(file) <= 0:
    file = "mbox-short.txt"
file_handler = open(file)

email_count = dict()
most_appeariences = ""
highest_count = 0

for line in file_handler:
    if line.startswith("From "):
        line_list = line.split()
        address = line_list[1]
        email_count[address] = email_count.get(address, 0) + 1

for address,appeariences in email_count.items():
    if appeariences > highest_count:
        most_appeariences = address
        highest_count = appeariences

print(most_appeariences, highest_count)
