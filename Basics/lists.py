# Declare and Set the List
cars = ['camaro', 'corvette', 'challenger', 'charger']

#Print List
print(cars)

# Print the 1st Elemnet
print(cars[1])

# Print and Capitalize the 2nd Element
print(cars[2].title())

# Print the last element
print(cars[-1])

# Pulling element from list and composing a message using that value
message = f"My dream car is a {cars[1]}."
print(message)

# Appending Element to the end of List
cars.append('mustang')
print(cars)

# Appending to an empty string
jdmCars = []
jdmCars.append('RX-7')
jdmCars.append('NSX')
jdmCars.append('Supra')
print(jdmCars)

# Inserting a new element into a list
jdmCars.insert(0, 'Skyline GT-R')
print(jdmCars)

# Deleting an element from the string.
del jdmCars[2]
print(jdmCars)

