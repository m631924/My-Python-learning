'''
Anagrams
An anagram is a new word formed by rearranging the letters 
of a word, using all the original letters exactly once. 
For example, the phrases "rail safety" and "fairy tales" 
are anagrams, while "I am" and "You are" are not.
'''

text1 = input("Enter text1... : ")
text2 = input("Enter text2... : ")
#text1 = "Listen"
#text2 = "Si  l ent"
text1 = text1.replace(" ", "")
text2 = text2.replace(" ", "")
text1 = text1.upper()
text2 = text2.upper()
if sorted(text1) == sorted(text2):
    print("Anagrams")
else:
    print("Not anagrams")
    
