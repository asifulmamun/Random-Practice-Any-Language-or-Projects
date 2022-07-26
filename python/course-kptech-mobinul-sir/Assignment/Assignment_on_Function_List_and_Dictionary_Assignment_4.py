""" P1:- Write a function named city_function() that takes in the name of a city ant its country. Print several times. """
def city_function():
    city = 'Dhaka'
    country = 'Bangladesh'
    print('Hello, you are now in %s, %s'%(city, country))

city_function()


""" P2:- Use the same function but now make a dictionary named globe = { “ city“: city_name, “country”: country_name }, return arguments in the dictionary and print all items through loop. """
def city_function(city_name, cuontry_name):
    globe = {
        'city' : city_name,
        'country' : cuontry_name
    }
    
    for key, value in globe.items():
        print(key, ': ', value)

city_function('Dhaka', 'Bangladesh')


""" P3:- Make a list of magician’s names. Pass the list to a function called show_magicians(), which prints the name of each magician in the list. """
def show_magicians(Magicians_list):
    print(Magicians_list)
    for Magician in Magicians_list:
        print(Magician)

Magicians_list = ['P C Sorkar', 'Jewel Eich', 'Harry Houdini', 'David Copperfield']
show_magicians(Magicians_list)