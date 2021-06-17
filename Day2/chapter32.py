theCount = [1, 2, 3, 4, 5]
fruits = ['banana', 'grape', 'mango', 'durian']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in theCount:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# amixed list
# use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# build lists with an empty one
elements = []

# use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# print them out
for i in elements:
    print(f"Element was: {i}")