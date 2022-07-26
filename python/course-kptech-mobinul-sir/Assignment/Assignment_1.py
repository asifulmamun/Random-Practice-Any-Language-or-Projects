"""
---------------- KPtech Pyway ---------------------
	1. Comment “Single line” and “Multi line” and save it in “Assignment_1.py”
	2. Save all in “Assignment_1.py” file.
	3. Take two string input and convert them into integer, write comment before
	each operations.
	execute these operations:
	+ , - , /, *, %
	4. Take input as range. Check those numbers even or odd. Use while loop.
	5. Print table of range 10. Use for loop
"""

# This is single line comment

'''
This is multiple line comment with
	single quote first question detailes has double quote multiple line comment
	(Q.1)
'''

# Saved all in Assignment_.py (Q.2)

'''
	------------ Q.3 ---------
	Take String Input then
	convert them and do operation with Some Arithmetic Operator
'''

# Get data from Keabord only string
operationInputA = input("Enter 1st number for operation with Arithmetic: ")
# Converting Data string to intiger from get Keaboard
operationInputA = int(operationInputA)
print(operationInputA, "\nTyepe Check :", type(operationInputA), "\n")

# Get data from Keabord with string and convert in inline direct and pritn  them
operationInputB = int(input("Enter 2nd number for operation with Arithmetic: "))
print(operationInputB, "Tyepe Check :", type(operationInputB), "\n")

print("\n Operation Results given below: \n")
# Addition Operation
print('1st Number + 2nd Number = ', operationInputA+operationInputB, "\n")

# Sub Operation
print('1st Number - 2nd Number = ', operationInputA-operationInputB, "\n")

# Mult Operation
print('1st Number * 2nd Number = ', operationInputA*operationInputB, "\n")

# Div Operation
print('1st Number / 2nd Number = ', operationInputA/operationInputB, "\n")

# Mod Operation
print('1st Number Modulas 2nd Number = ', operationInputA%operationInputB, "\n")


'''
	------------ Q.4 ---------
	Take a real number for range
	Then check there even or odd with while loop
'''
# Geting Data for range
rangeEvenOrOdd = int(input("Enter any real and positive number for checking all even or odd : "))
print("\n\n Range and Type: ", rangeEvenOrOdd, type(rangeEvenOrOdd), "\n Now checking them Even or Odd between 1 to ", rangeEvenOrOdd, ":\n" )

# while loop
# Starting from 1
CheckEvenOrOdd = 1
while CheckEvenOrOdd<=rangeEvenOrOdd:
	# Check for Even
	if CheckEvenOrOdd%2 == 0:
		print("Number: ", CheckEvenOrOdd, " (is Even)\n")
		# Check for Odd
	elif CheckEvenOrOdd%2 != 0:
		print("Number: ", CheckEvenOrOdd, " (is Odd)\n")
	# update part while loop
	CheckEvenOrOdd +=1

'''
	------------ Q.5 -----
	While loop Range = 10
'''
# For Loop
print('\n\n While Loop range 10: \n')
for forLoop in range(1,11):
	print("Number :", forLoop)

print('\n\n Program By - Al Mamun (@asifulmamun) \n\n')
# ---------------------- END @asifulmamun ----------------------
