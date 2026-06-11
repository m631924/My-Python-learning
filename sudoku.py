'''
Sudoku
This program checks if a sudoku is solved
and will print "Yes" or "No".
'''
sudoku = []

# Input
while True:

    row = input("Enter a sudoku row with 9 numeric values... : ")

    if len(row) == 9:
      if row.isnumeric():
        sudoku.append(row)
        print("Row " +str(len(sudoku))+ " entered successfully!")
      else:
        print("Invalid input, enter only numbers",  end="\n")


    else:
      print("Invalid input, row containes more or less than 9 values", end="\n")

    # Check if sudoku input is complete
    if len(sudoku) == 9:
        break

# Uncomment test1 or test 2 and comment "#" input to test the programm

'''
# Test 1 - result: Yes
sudoku = ["295743861",
 "431865927",
"876192543",
"387459216",
"612387495",
"549216738",
"763524189",
"928671354",
"154938672",]
'''

'''
# Test2 - result: No
sudoku = ["195743862",
"431865927",
"876192543",
"387459216",
"612387495",
"549216738",
"763524189",
"928671354",
"254938671",]
'''
# Visualize sudoku
print("---Sudoku--")
for i in sudoku:
    print(i, end="\n")
print("-----------")


found = True

def verify(numList):
    '''Verify if we have numbers 1 to 9 in a  list'''
    #numlist: string Ex: "142986735"
    found = True
    for i in range(9):
        search = str(i+1)
        if search not in numList:
            found = False
            break
    return found


# Row verification
for i in range(9):
    if found == False:
        break
    found = verify(sudoku[i])
    if not found:
        break


if found:
    # Column verification
    for i in range(9): # column
        if found == False:
            break
        sudokuColumn = ""
        for j in range(9): #row
           sudokuColumn += sudoku[j][i]

           if j == 8:
               found = verify(sudokuColumn)
               if not found:
                   break

sudokuTile = ""
tiles = []
if found:
    # Tile verification
    # extract 9 tiles or subgroups
    for i in range(3): # tile row
        for j in range(3): # tile column
            sudokuTile = ""
            for k in range(3): # row
                for l in range(3): # column
                    sudokuTile += sudoku[i*3+k][j*3+l]
                    if len(sudokuTile) == 9:
                        tiles.append(sudokuTile)
                        #print(sudokuTile)

    for numbers in tiles:
        found = verify(numbers)
        if not found:
            break

# Result:
if found:
    print("Yes")
else:
    print("No")
