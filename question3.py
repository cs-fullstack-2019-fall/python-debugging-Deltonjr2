# ### Problem 3:
# Ask the user for a negative number. Print from 7 down to the user's negative number. You must include the user's number.

userInput = int(input("Enter a negative number"))
for index in range(7, userInput-1, -1):
    print(index)
# The error was the code had brackets instead of parenthesis ran in console code now resolved
