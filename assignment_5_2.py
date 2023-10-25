"""Assignment 5.2"""

max_val = 0
min_val = 0

while True:
    # Write a program that repeatedly prompts a user for integer numbers until
    # the user enters 'done'.
    sval = input("Enter a number: ")
    if sval == "done":
        break

    # If the user enters anything other than a valid number catch it with a try/except
    # and put out an appropriate message and ignore the number.
    try:
        num = int(sval)
    except:
        print("Invalid input")
        continue

    num = int(sval)

    if num > max_val:
        max_val = num
    elif min_val == 0:
        min_val = num
    elif num < min_val:
        min_val = num

# Once 'done' is entered, print out the largest and smallest of the numbers.
print("Maximum is", max_val)
print("Minimum is", min_val)
