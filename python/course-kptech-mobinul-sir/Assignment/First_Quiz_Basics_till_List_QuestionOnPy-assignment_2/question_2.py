"""
	2. Make a list of 5 students height. Calculate the average of it.
"""
# Imported Statistic Library then shorten with variable statistic keyword
import statistics
sLib = statistics

#Design or Space
studentsHeight = [5, 5.10, 5.4, 5.6, 5.5]

print(studentsHeight)
# Average with library statistics
print("\nCalculate with Statistics Library imported = ", float(sLib.mean(studentsHeight)))

# Average with general sum and divided
print("\nCalculate with general summation and dividing = ", float(sum(studentsHeight)/len(studentsHeight)))

