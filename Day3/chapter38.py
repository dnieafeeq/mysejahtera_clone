ten_things = "Apples Oranges Crows Motorcycles Battery Salt"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Badminton",
              "Flower", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Addinggggg: ", next_one)

    stuff.append(next_one)
    print(f"There are {len(stuff)} items now!")

print("Here we go: ", stuff)
print("Let's go do somethings with stuff!!!")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print(' | '.join(stuff[3:5]))

