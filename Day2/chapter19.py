def cheese_and_crackers(cheeseCount, boxesCrackers):
    print(f"You have {cheeseCount} cheeses!")
    print(f"You have {boxesCrackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n\n")

# start
print("We can just give the function numbers directly:")
cheese_and_crackers(40, 60)


print("OR, we can use variables from our script:")
amountCheese = 20
amountCrackers = 16

cheese_and_crackers(amountCheese, amountCrackers)

# can do math inside it
print("We can even do math inside:")
cheese_and_crackers(12 + 23, 9 + 6)

# combine variable and math
print("And we can combine the two, variables and math:")
cheese_and_crackers(amountCheese + 120, amountCrackers + 200)