print("Let's practice Chapter 24.")
print('You\'d need to know \'bouttt escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secretFormula(started):
    jellyBeans = started * 530
    jars = jellyBeans / 200
    crates = jars / 100
    return jellyBeans, jars, crates


start_point = 1000
beans, jars, crates = secretFormula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 20

print("We can also do that this way:")
formula = secretFormula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))