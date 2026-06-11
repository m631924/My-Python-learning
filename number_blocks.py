blocks = int(input("Enter the number of blocks: "))
'''
Levels: blocks needed
1:1
2:2+(1)=3
3:3+(3)=6
4:4+(6)=10
5:5+(10)=15
6:6+(15)=21
7:7+(21)=28
8:8+(28)=36
'''

#
# Write your code here.
height = 0
blocks_needed = 0
while True:
    height +=1
    blocks_needed += height
    if blocks_needed > blocks:
        height-=1
        break
#	

print("The height of the pyramid:", height)

