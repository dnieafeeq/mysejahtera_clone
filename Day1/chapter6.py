typesPeople = 10
x = f"There are {typesPeople} types of people."

binary = "binary"
donot = "don't"
y = f"Those who know {binary} and those who {donot}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

test = f"Lorem ipsum {y} and {x}"

print("TESTING:", test)