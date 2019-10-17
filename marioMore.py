'''
This program takes in a number from 0 to 23, inclusive. It creates 2 half
pyramids that are mirror images of each other that is the height the user
entered with a hole in the middle. 

Hina Sekine 
'''

# Greeting
print('This program will make a pyramid like the old school Mario games')
print('The height entered shoule be between 0 and 23, inclusive.\n')

# User Input + error checking 
pyramidHeight = input("Height: ")
while pyramidHeight.isdigit() == False or not(0 <= int(pyramidHeight) <= 23):
    pyramidHeight = input("Height: ")

pyramidHeight = int(pyramidHeight)

# Creates & displays the pyramid 
frontSpace = pyramidHeight - 1
for i in range(1, pyramidHeight + 1):
    hashNumber = '#' * i 
    pyramidRow = (frontSpace * ' ') + hashNumber + '  ' + hashNumber     
    frontSpace = frontSpace - 1
    
    print(pyramidRow)
