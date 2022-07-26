# # Simple Modification appending data in function
# def members(memberList):
#     memberList.append('Shaun')
#     return memberList

# memberList = ['mamun', 'munna']

# print(members(memberList))

# # modification big with pop in loop
# def mylist(simpleList, emptyList):
#     while simpleList:
#         newList = simpleList.pop() # Last pop and poped added to newList
#         print(newList) # print pop out and stored in new list data last data first pop and add to new list as first
#         emptyList.append(newList) # get new list and appending one by one in empty list

# def show_emptyList(emptyList):
#     for thisEmpty in emptyList:
#         print(thisEmpty)

# simpleList = ['mamun', 'shaun', 'munna']
# emptyList = []

# mylist(simpleList, emptyList)
# show_emptyList(emptyList)