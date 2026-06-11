'''
The Digit of Life
Some say that the Digit of Life is a digit evaluated using 
somebody's birthday. It's simple – you just need to sum all 
the digits of the date. If the result contains more than one 
digit, you have to repeat the addition until you get exactly 
one digit.
'''

while True:
    try:
        date = input("Enter your birthday in format YYYYMMDD, or YYYYDDMM, or MMDDYYYY : ")
        if len(date)==8: ## verify lenght of date
            try:
                date = int(date)
                break
            except ValueError:
                print("Invalid date")
        else:
            print("Invalid date")
            
    except:
        print("Invalid input")
        
        
#date = 19991229 #result 6
#date = 20000101 #result 4

number = 0

while True:
    number = 0
    for i in str(date):
        number += int(i)
    if number <= 9:
        break
    else:
        date = number
print(number)
