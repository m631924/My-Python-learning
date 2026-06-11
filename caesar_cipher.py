'''
Caesar cipher
The original Caesar cipher shifts each character by 
one: a becomes b, z becomes a, and so on. Let's make it 
a bit harder, and allow the shifted value to come from 
the range 1..25 inclusive.
Moreover, let the code preserve the letters' case 
(lower-case letters will remain lower-case) and all 
non-alphabetical characters should remain untouched.

'''

msg = input("Write your text to encript... : ")
while True:
    
    try:
        shiftValue = int(input("Enter shift value from 1 to 25... : "))
        if (shiftValue >= 1) and (shiftValue <= 25):
            break
        else:
            print("Number out of range")
        
    except ValueError:
        print("Not a number")
    
    
# Test 1
#msg = "abcxyzABCxyz 123"
#shiftValue = 2
# output = "cdezabCDEzab 123"

# Test 2
#msg = "The die is cast"
#shiftValue = 25
# output = "Sgd chd hr bzrs"

cipher = ""
lowCaseLimit1 = ord("a") # 97
lowCaseLimit2 = ord("z") # 122
upperCaseLimit1 = ord("A") # 65
upperCaseLimit2 = ord("Z") # 90

def convert(char, shift):
    n1 = ord(char)
    n2, n3 = 0, 0
    limit1, limit2 = 0, 0
    char2 = ""
    # upper case
    if (n1 >= upperCaseLimit1) and (n1 <= upperCaseLimit2):
        limit1 = upperCaseLimit1
        limit2 = upperCaseLimit2
    # lower case
    elif (n1 >= lowCaseLimit1) and (n1 <= lowCaseLimit2):
        limit1 = lowCaseLimit1
        limit2 = lowCaseLimit2
    else:
        print("Not a character, will return 'A' by default")
        return "A"
    
    # new ascii
    n2 = n1 + shift
    
    # new ascii still in range
    if n2 <= limit2:
        n3 = n2
        
    # new ascii, need to find new ascii number
    else:
        n3 = (n2-limit2) + limit1 - 1
    
    char2 = chr(n3)
    return char2
    

for char in msg:
    
    if char.isalpha():
        #print("debug1-alphabetic")
        cipher += convert(char, shiftValue)
    elif char.isnumeric():
        #print("debug2-numeric")
        cipher += char
    else:
        #print("debug3-other")
        cipher += char

print(cipher)       
