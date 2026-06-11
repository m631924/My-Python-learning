'''
Find a word!
Let's play a game. We will give you two strings: one being
a word (e.g., "dog") and the second being a combination of 
any characters.

Your task is to write a program which answers the following 
question: are the characters comprising the first string 
hidden inside the second string?
'''
text1 = input("Enter first string... : ")
text2 = input("Enter second string... : ")
#text1 = "donor"
#text2 = "Nabucodonosor"
#text1 = "donut"
#text2 = "Nabucodonosor"

text1 = text1.upper()
text2 = text2.upper()

result = True
for char in text1:
    if char not in text2:
        result = False
        break
if result == True:
    print("Yes")
else:
    print("No")
