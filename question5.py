# ### Problem 5:
# Create the list: squad = ["One", "Two", "Three", "Four", "Five"]. Print the list in reverse without using a list method.
squad = ["One", "Two", "Three", "Four", "Five"]
for index in range(len(squad)-1, -1, -1):
    print(squad(index))  # you need to use square brackets here around index instead of parenthesis
    # //Error was code should have read for index in range it said index of range. Uodated to in range.