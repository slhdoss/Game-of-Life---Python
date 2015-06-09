__author__ = 'Sebastiano'


import sys

class unit(object):
    def __init__(self):
        self.alive = False # describes current state of the node
        self.willLive = False # describes future statre of node which is updated by function updatelife

    def updateLife(self, grid, xG, yG):

        def updateWindow(grid, xC, yC):
            window = [[[0,0] for x in range(3)] for y in range(3)]
            xG = xC -1
            yG = yC -1

            for xW in range(3):
                for yW in range(3):

                    if (xG > xC + 1):
                        xG = xC -1
                        yG += 1

                    xG += 1

                    if(xG >= grid.xRange):
                        window[xW][yW][0] = 0
                    elif(xG < 0):
                        window[xW][yW][0] = grid.xRange - 1
                    else:
                        window[xW][yW][0] = xG


                    if(yG < 0):
                        window[xW][yW][1] = grid.yRange -1
                    elif(yG >= grid.yRange):
                        window[xW][yW][1] = 0
                    else:
                        window[xW][yW][1] = yG

            return window

        window = updateWindow(grid, xG, yG)
        alPoints = 0

        for x in range(3):
            for y in range(3):
                if grid.field[window[x][y][0]][window[x][y][1]].alive and x != 1 and y != 1:
                    alPoints+=1

        if alPoints < 2:
            grid.field[xG][yG].willLive = False
        elif alPoints >= 2 and alPoints <= 3:
            grid.field[xG][yG].willLive = True
        elif alPoints >= 3 and grid.field[xG][yG].alive:
            grid.field[xG][yG].willLive = False
        elif alPoints == 3 and grid.field[xG][yG].alive == False:
            grid.field[xG][yG].willLive = True
        else:
            grid.field[xG][yG].willLive = True



class grid(object):
    def __init__(self, xRange, yRange):
        self.xRange = xRange
        self.yRange = yRange
        self.field = [[unit() for x in range(xRange)] for y in range(yRange)]
        self.initGrid()

    def initGrid(self):

        xRatio = self.xRange / 5
        yRatio = self.xRange / 5

        for x in range(self.xRange):
            for y in range(self.yRange):
                if x >= xRatio*2 and x <= xRatio * 3 and y >= yRatio * 1 and y <= yRatio * 2 :
                    self.field[x][y].alive = 1
                if x >= xRatio*2 and x <= xRatio * 3 and y >= yRatio * 3 and y <= yRatio * 4 :
                    self.field[x][y].alive = 1

        #generator to fill initial gird with life

    def updateGrid(self):

        for xG in range(self.xRange):
            for yG in range(self.yRange):
                self.field[xG][yG].updateLife(self,xG,yG)

        for xG in range(self.xRange):
            for yG in range(self.yRange):
                self.field[xG][yG].alive = self.field[xG][yG].willLive


def main(argv):

    newGrid = grid(40,40)
    newGrid.updateGrid()
    newGrid.updateGrid()
    newGrid.updateGrid()
    newGrid.updateGrid()
    newGrid.updateGrid()
    newGrid.updateGrid()
    newGrid.updateGrid()

    print [[int(newGrid.field[x][y].alive) for x in range(newGrid.xRange)] for y in range(newGrid.yRange)]
    # for x in range(newGrid.xRange):
    #     for y in range(newGrid.yRange):

    pass

if __name__ == "__main__":
    main(sys.argv)

