#Exercise
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]     
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(" ", end="") #end="" means that we don't want to print a new line after each character, we want to print them on the same line
        else:
            print("*", end="")
    print("") #print a new line after each row