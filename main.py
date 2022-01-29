
# Add failsafes later
import random
from random import sample
import pprint
import turtle
import math
import os
from guiapplication import a, b, _difficulty


t = turtle.Turtle()
t.speed(0)
WIDTH, HEIGHT = 1100, 1100
ts = turtle.Screen()
ts.setup(WIDTH, HEIGHT)
ts.title("Sudoku Machine 3000")
rows = 0
columns = 0
sizeMultiplier = 40
style = ('Courier', sizeMultiplier // 2, 'normal')

base = int(a)
print(f"You picked {base**2}x{base**2} sudokus")
times = int(b)
print(f"You picked {times} batches")
difficulty = _difficulty
print(f"You picked {difficulty.upper()} sudokus")
print("Starting program...")



def GotoCoor(x, y):
    t.penup()
    t.goto(columns * sizeMultiplier / -2 + sizeMultiplier * x, rows * sizeMultiplier / -2 + sizeMultiplier * y)
    t.pendown()

def MakeBorders():
    t.penup()
    t.goto(columns*sizeMultiplier/-2,rows*sizeMultiplier/-2)
    t.pendown()
    t.pensize(5)
    for i in range(2):
        t.fd(sizeMultiplier*columns)
        t.left(90)
        t.fd(sizeMultiplier*rows)
        t.left(90)
    t.pensize(1)

def drawGrid(grid, colour):
    t.hideturtle()
    t.pencolor("black")
    t.penup()


    global rows
    global columns
    rows = len(grid)
    columns = len(grid[0])

    MakeBorders()
    subSquareLength = int(math.sqrt(rows))
    for i in range(rows + 1):
        if (i % subSquareLength == 0):
            t.pensize(5)
        else:
            t.pensize(1)
        t.penup()
        t.goto(columns * sizeMultiplier / -2, (rows * sizeMultiplier / -2) + sizeMultiplier * i)
        t.pendown()
        t.fd(sizeMultiplier * rows)
    t.setheading(90)

    for i in range(columns + 1):
        if (i % subSquareLength == 0):
            t.pensize(5)
        else:
            t.pensize(1)
        t.penup()
        t.goto(columns * sizeMultiplier / -2 + sizeMultiplier * i, (rows * sizeMultiplier / -2))
        t.pendown()
        t.fd(sizeMultiplier * columns)
    t.setheading(0)
    t.pencolor(colour)
    for rowNo in range(rows):
        for columnNo in range(columns):
            GotoCoor(columnNo + 0.5, rows - rowNo - 1)
            t.write(grid[rowNo][columnNo], font=style, align="center")


for j in range(times):

    if (os.path.exists("/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus")) == True:
        pass
    else:
        directory = "Sudokus"
        parent_dir = "/Users/tharun/Desktop/SDD MAJOR WORK2"
        path = os.path.join(parent_dir, directory)
        os.makedirs(path)

    directory = "Sudoku_" + str([j + 1])
    parent_dir = f"/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus"
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)
    side = base ** 2
    lst = list()
    counter = 0
    if (difficulty.lower() == "e"):
        limit = (side ** 2)/4
    if (difficulty.lower() == "m"):             #side == 4
        limit = (side ** 2)/4 * 3/2
    if (difficulty.lower() == "h"):
        limit = (side ** 2)/4 * 3

    def pattern(r,c):
        return (base*(r%base)+r//base+c)%side

    def shuffle(s):
        return sample(s,len(s))


    #cite this
    rBase = range(base)
    rows  = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols  = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums  = shuffle(range(1,base**2+1))


    board = [[nums[pattern(r,c)] for c in cols] for r in rows]
    drawGrid(board, "red")
    GotoCoor(base, -1)
    t.write("Solution", font=style, align="center")

    x = "Sudoku_" + str([j + 1])
    directory = "Answers"
    parent_dir = f"/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/{x}"
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)
    ts.getcanvas().postscript(file=f"/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/{x}/Answers/sol" +  "-" + str(difficulty.upper()) + "-"+ str(base**2) + "x" + str(base**2) + "-" +str(j + 1) + ".ps")

    turtle.clearscreen()

    for x in board:
        lst += x
    "_____________"


    while counter < limit: #max things that can be removed from a sudoku
        i = random.randint(0, base**4-1)
        if lst[i] == 0:
            continue
        else:
            lst[i] = 0
        counter += 1

    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = ''
            continue

    grid = [lst[i:i + (base ** 2)] for i in range(0, len(lst), (base ** 2))]
    pprint.pprint(grid)


    drawGrid(grid, "black")
    GotoCoor(base, -1)
    t.write("Solveable", font=style, align="center")
    ts = turtle.Screen()

    x = "Sudoku_" + str([j + 1])
    directory = "BlankSudoku"
    parent_dir = f"/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/{x}"
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)
    ts.getcanvas().postscript(file=f"/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/{x}/BlankSudoku/blank" + "-" + str(difficulty.upper()) + "-" + str(base ** 2) + "x" + str(base ** 2) + "-" + str(j + 1) + ".ps")

    turtle.clearscreen()

