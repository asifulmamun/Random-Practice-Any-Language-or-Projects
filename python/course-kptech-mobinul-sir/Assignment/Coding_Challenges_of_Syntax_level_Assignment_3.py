"""
    @ Coding Challenges of Syntax level
    @ Assignment-3
    @ Victory Day Cooding Compettition(16th December, 2019)
"""


# 1. Input an Integer n and perform these tasks:
n = int(input("Enter any integert Number for check Even or Odd: "))

# Check Even or Odd, Queation-1.(i and ii)
if n % 2 == 0:
    print("Even\n")
else:
    print("Odd\n")

# check Between 1-5 or not, Queation-1.(iii and iv)
if n in range (1,5):
    print("Firts Five\n")
else:
    print("Not in Five\n")


# 2. Make a list of Motorcycle with at least 4 data and perform these tasks:
motorCycleList = ["Honda", "Suzuki", "R15", "Pulsar", "Apache"]

motorCycleListAppended = motorCycleList.copy()
motorCycleListAppended.append("Harley-Davidson") # Adding Value
for listmoto in motorCycleListAppended:
    print('\nList: ', listmoto)

motorCycleListRemoved = motorCycleList.copy()
motorCycleListRemoved.pop() # remove last
print('Remove: ', motorCycleListRemoved)

motorCycleListReverse = motorCycleList.copy()
motorCycleListReverse.reverse() # Reverse
print('Reverse: ', motorCycleListReverse)

mycopyHonda = motorCycleList[:3].copy()
print('copy: ', mycopyHonda)



# 3. Create a Dictionary with these Keys: (i-iii)
mydic = {
    'Full Name' : 'Mamun',
    'Education' : {
        'ssc' : 2015,
        'hsc' : 2017
    },
    'Languages': ['English', 'Bangla', 'Hindi', 'Arabic']
}

# print all kvp
for key, value in mydic.items():
    print(key, ': ', value)

# print only under kvp
edudic = mydic['Education']
for key, value in edudic.items():
    print(key, ': ', value)

# print under kvp list
lanlist = mydic['Languages']
for lang in lanlist:
    print('Languages: ', lang)

# add eye color in exist dictionary
print('\nAdd Eye Color in Dictionary')
mydic['Eye Color'] = 'black'
for key, value in mydic.items():
    print(key, ': ', value)

# remove eye color in exist dictionary
print('\nRemove Eye Color from Dictionary')
del mydic['Eye Color']
for key, value in mydic.items():
    print(key, ': ', value)



''' 4. Make a list of special symbols such as - !,@,#,$,& etc. Use all of them from keyboard. Then perform the tasks: '''
symlist = []
a = 1
while a<6:
    sym = input('Enter any Special Sybmol Total 5 time hit: ')
    
    if sym == '#':
        print('This is Comment sign.')
    elif sym == '$':
        print('This is Doller sign.')

    symlist.append(sym)
    a+=1
print(symlist)