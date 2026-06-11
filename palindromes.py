'''
Palindromes
It's a word which look the same when read forward and backward.
For example, "kayak" is a palindrome, while "loyal" is not.
This code ignores spaces
'''
text = input("Checking a palindrome. Enter you text... : ")
#text = "Ten  animals I slam in a net" # it's a palindrome
#text = "Eleven animals I slam in a net" # it's not a palindrome
text = text.replace(" ", "") # delete spaces
text = text.replace("   ", "") # delete tabulations
text2 = text.upper() # standardized text
text3 = text2[::-1] # reversed text

if (text2 == text3) and (len(text2)>0) :
    print("It's a palindrome")
else:
    print("It's not a palindrome")
