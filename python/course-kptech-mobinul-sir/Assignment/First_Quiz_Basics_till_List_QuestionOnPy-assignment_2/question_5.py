"""
	5. Input a String, check the string is Palindrome or not.
"""

checkPalindrome = input("Enter any Text : ")

# Reverse this inputed string
rev = checkPalindrome[::-1]

if rev == checkPalindrome:
	print(checkPalindrome, " = is Palindrome Text.")
else:
	print(checkPalindrome, " = is not Palindrome Text.")