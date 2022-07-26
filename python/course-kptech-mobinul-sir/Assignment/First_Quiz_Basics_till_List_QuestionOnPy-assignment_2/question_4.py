"""
	4. Create a list named food, such as

		foods = [ ‘Burger’, ‘Sandwich’, ‘Pizza’ ]
		Add ‘Candy’ and ‘Coca Cola’ in the list. Remove Pizza from the list.
"""

# Declare
foods = ['Burger', 'Sandwich', 'Pizza']

# Add Candy and Coca Cola
foods.extend(['Candy', 'Coca Cola'])
# Removed Pizza
foods.remove('Pizza')

print(foods)