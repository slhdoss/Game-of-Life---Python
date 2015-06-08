__author__ = 'Sebastiano'


import sys


def initGrid(xRange ,yRange):

    #empty grid
    grid = [[0 for x in range(xRange)] for y in range(yRange)]
    xRatio = xRange / 5
    yRatio = xRange / 5

    for x in range(xRange):
        for y in range(yRange):
            if x >= xRatio*2 and x <= xRatio * 3 and y >= yRatio * 1 and y <= yRatio * 2 :
                grid[x][y] = 1
            if x >= xRatio*2 and x <= xRatio * 3 and y >= yRatio * 3 and y <= yRatio * 4 :
                grid[x][y] = 1

    #generator to fill initial gird with life
    return grid

def updateGrid(grid, xRange, yRange):

    newGrid = [[0 for x in range(xRange)] for y in range(yRange)]
    window = initWindow()

    for xG in range(xRange):
        for yG in range(yRange):
            window = updateWindow(window, xRange, yRange, xG, yG)
            if isAlive(window, grid):
                newGrid[xG][yG] = 1;
            else:
                newGrid[xG][yG] = 0;

    return newGrid

def isAlive(window,grid):

    alPoints = 0

    for x in range(3):
        for y in range(3):
            if grid[window[x][y][0]] [window[x][y][1]] == 1 and x != 1 and y != 1:
                alPoints+=1

    if alPoints < 2:
        return False
    elif alPoints >= 2 and alPoints <= 3:
        return True
    elif alPoints >= 3 and grid[window[1][1][0]][window[1][1][1]] == 1:
        return False
    elif alPoints == 3 and grid[window[1][1][0]][ window[1][1][1]] == 0:
        return True
    else:
        return True

def initWindow():
    window = [[[0,0] for x in range(3)] for y in range(3)]

    """
    for xW in range(3):
        for xY in range(3):
            xG = xW -1
            yG = yW -1
            if xW == 0:
                xG = xRange
            if yW == 0:
                yG = yRange
            window[xW][yW] = [xG,yG]
    """

    return window

def updateWindow(window, xRange, yRange, xC, yC):

    xG = xC -1
    yG = yC -1

    for xW in range(3):
        for yW in range(3):

            if (xG > xC + 1):
                xG = xC -1
                yG += 1

            xG += 1

            if(xG >= xRange):
                window[xW][yW][0] = 0
            elif(xG < 0):
                window[xW][yW][0] = xRange - 1
            else:
                window[xW][yW][0] = xG

            if(yG < 0):
                window[xW][yW][1] = yRange -1
            elif(yG >= yRange):
                window[xW][yW][1] = 0
            else:
                window[xW][yW][1] = yG

    return window





def main(argv):
    grid = initGrid(40,40)
    grid = updateGrid(grid, 40, 40)
    grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    # grid = updateGrid(grid, 40, 40)
    print grid
    pass

if __name__ == "__main__":
    main(sys.argv)

