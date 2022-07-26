totalPrint = int(input("How many pages you want print: "))

# firstPrint = int(input("Enter pages number which you want to print first: ")) # Page number which page print first

totalPages = []


for pages in range(1, (totalPrint+1)):
    totalPages.append(str(pages))

print(totalPages)


totalPages.remove('25')

print(totalPages)


