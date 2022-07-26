# # simple dictonary
# myinfo = {'Username' : 'asifulmamun',
#             'Name' : 'Al Mamun',
#             'Mobile' : '01721600688'
# }

# print(str(myinfo['Username']))

# for keys, values in myinfo.items():
#     print(keys, values)

# for key in myinfo.keys():
#     print(key)

# for value in myinfo.values():
#     print(value)

# Sorted
# for keys, values in sorted(myinfo.items()):
#     print(keys, values)



# # 2 Dic in 1 list
# car1 = {'Color' : 'green', 'style' : 'old'}
# car2 = {'Color' : 'black', 'style' : 'new'}

# # in list
# carslist = [car1, car2]
# print(carslist)


# # Dictionalry under Dictionary - COMPLEX
# users = {
#     'mamun' : {
#         'Name' : 'Al Mamun',
#         'Age' : '22',
#         'Dist' : 'Kishoreganj'
#     },
#     'rafi' : {
#         'Name' : 'Rafi',
#         'Age' : '23',
#         'Dist' : 'Sirajganj'
#     }
# }

# # print(users['mamun']['Age'])

# for keys, values in users.items():
#     # print(keys)
#     # print(values)
#     # print(keys, values['Name'], values['Age']) # with specific keys name, age it's values

#     for nextkeys, nextvalues in values.items():
#         print(nextkeys) # print 1st dictionary keys valus under 2nd dictionary keys
#         print(nextvalues) # print 1st dictionary keys valus under 2nd dictionary keys values



# # modification adding etc
# car1 = {'Color' : 'green', 'style' : 'old'}
# print(car1)

# # Modify
# car1['Color'] = 'black'
# print(car1)

# # Adding
# car1['model'] = 'E1'
# print(car1)

# # Remove
# del car1['model']
# print(car1)

# # Remove
# car1.pop('style')
# print(car1)

# # Remove all
# car1.clear()
# print(car1)