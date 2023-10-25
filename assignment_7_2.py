"""Assignment 7.1"""

# Write a program that prompts for a file name, then opens
# that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each
# of the lines and compute the average of those values and
# produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
file = input("Enter file name: ")
file_handler = open(file)
count = 0
added = 0
for line in file_handler:
    if line.startswith("X-DSPAM-Confidence:"):
        start = line.find(":")
        chunk = line[start + 1:]
        num = float(chunk.strip())
        count = count + 1
        added = added + num
average = added / count
print("Average spam confidence:", average)
