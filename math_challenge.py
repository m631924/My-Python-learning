'''
take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, go back to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.
'''

number = 15
c0 = number
steps = 0


while c0 != 1:
    if c0 <= 0:
        break
        print('ending...')
    steps+=1
    # even
    if  c0 % 2 == 0:
        c0 = int(c0/2)

    # odds
    else:
        c0 = int(c0*3+1)
    print(c0)
    
print(f'steps = {steps}')
