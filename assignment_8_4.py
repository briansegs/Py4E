"""Assignment 8.4"""

# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the
# list and if not append it to the list.
# When the program completes, sort and print the resulting words in
# python sort() order as shown in the desired output.

file = input("Enter file name: ")
file_handler = open(file)

words = []
for line in file_handler:
    split_words = line.split()
    for word in split_words:
        if word not in words:
            words.append(word)
words.sort()

print(words)
