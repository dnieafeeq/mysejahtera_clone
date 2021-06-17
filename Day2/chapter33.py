y = 0
numbers = []

while y <= 5:
    print(f"At the top y is {y}")
    numbers.append(y)

    y = y + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom y is {y}")


print("The numbers: ")

for num in numbers:
    print(num)