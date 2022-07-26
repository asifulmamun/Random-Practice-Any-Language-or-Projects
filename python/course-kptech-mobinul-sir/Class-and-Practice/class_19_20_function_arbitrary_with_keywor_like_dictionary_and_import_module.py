# # Arbitrary With keyword like as Dictionary multiple dictionary
# def members(name, **data):
#     mdmberData = {}
#     mdmberData['name'] = name

#     for key, value in data.items():
#         mdmberData[key] = value

#     return mdmberData

# newmem = members('mamun', area = 'kishoreganj', skill = 'py')
# print(newmem)
# print(newmem['skill'])
# print(members('mamun', area = 'kishoreganj', skill = 'py'))
# print(members('mamun', area = 'kishoreganj', skill = 'py')['name'])


# # imported all by module
# import class_19_importer
# class_19_importer.myimport()
# print(class_19_importer.imvar)


# # imported all by module with alia or nickname for short
# import class_19_importer as class19
# class19.myimport()
# print(class19.imvar)


# # Import All
# from class_19_importer import *
# myimport()
# print(imvar)


# # import specific function comma ',' for more specific imported declare like as myimport, myimport2
# # We can use function name as variabole Nickname and use this nickname
# from class_19_importer import myimport, myimport2 as im2
# myimport()
# im2()


# # import specific variable comma ',' for more specific imported declare like as imvar, myvar etc
# # We can use variable as variabole Nickname and use this nickname
# from class_19_importer import imvar, imvar2 as var2, imvar3
# print(imvar)
# print(var2)
# print(imvar3)


