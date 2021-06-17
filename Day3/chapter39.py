# create a map for abbreviation of state
states = {
    'Kedah': 'KDH',
    'Penang': 'PNG',
    'Sabah': 'SBH',
    'Kelantan': 'KEL',
    'Kuala Lumpur': 'KL',
    'Selangor': 'SGR'

}

# create a basic set of states and some cities in them
cities = {
    'SBH': 'Kota Kinabalu',
    'SGR': 'Petaling Jaya',
    'KEL': 'Tanah Merah',
    'KDH': 'Kulim'

}

# add some more cities
cities['PNG'] = 'Bayan Lepas'
cities['KL'] = 'Cheras'

# print out some cities
print('-' * 10)
print("PNG State has: ", cities['PNG'])
print("KL State has: ", cities['KL'])

# print some states
print('-' * 10)
print("Kelantan's abbreviation is: ", states['Kelantan'])
print("Sabah's abbreviation is: ", states['Sabah'])

# do it by using the state then cities dict
print('-' * 10)
print("Kelantan has: ", cities[states['Kelantan']])
print("Sabah has: ", cities[states['Sabah']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Perak')

if not state:
    print("Sorry, no Perak.")

# get a city with a default value
city = cities.get('PRK', 'Does Not Exist')
print(f"The city for the state 'PRK' is: {city}")
