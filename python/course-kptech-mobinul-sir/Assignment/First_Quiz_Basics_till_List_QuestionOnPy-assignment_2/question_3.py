"""
	3. Input 2 numbers and continuously finds out “Greater” or “Smaller” in several times. Break when they will be Equal.
"""

# loop for unlimited or not
i = 0
while i < 1:
	# Take input from user
	inputA = float(input("Enter 1st number for mathematics operations: "))
	inputB = float(input("Enter 2nd number for mathematics operations: "))


	if inputA > inputB :
		print("1st Number is Bigger then from 2nd Number")
		
	elif inputB == inputA:
		break

	else :
		print("2nd Number is Bigger then from 1st Number")
	i -= 1
	