myset = {'khan'}
print(myset)

myset2 = set('asifulmamun')
print(myset2)

# set comprehension
compressed = {f for f in "abcdef" if f not in "abcd"}
print(compressed)

compressed = {f for f in "abcdef" if f in "abcdk"}
print(compressed)

first = set("abcdefg")
second = set("abck")

print(first - second) # first to last substraction
print(first | second) # All print
print(first & second) # Wich matched
print(first ^ second) # which not matched both set

# in one element for {}
numberset = {'1244'}
print(numberset, type(numberset))

# divided element for set()
numberset = set('1244')
print(numberset, type(numberset))