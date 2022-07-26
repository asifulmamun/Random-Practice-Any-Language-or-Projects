"""
	1. Take 2 input, calculate in all mathematics operations.
"""

inputA = float(input("Enter 1st number for mathematics operations: "))
inputB = float(input("Enter 2nd number for mathematics operations: "))

# Addition Operation
print('1st Number + 2nd Number = ', inputA+inputB, "\n")

# Sub Operation
if inputA>inputB:
	print('1st Number - 2nd Number = ', inputA-inputB, "\n")
else:
	print('2n Number - 1st Number = ', inputB-inputA, "   - 2nd Number Subtraction Because this second number is bigger then from 1st Number\n")

# Mult Operation
print('1st Number * 2nd Number = ', inputA*inputB, "\n")

# Div Operation
if inputA>inputB:
	print('1st Number / 2nd Number = ', inputA/inputB, "\n")
else:
	print('2n Number / 1st Number = ', inputB/inputA, "   - 2nd Number Divided Because this second number is bigger then from 1st Number\n")