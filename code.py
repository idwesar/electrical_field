import numpy as np
import statistics as stats

'''SETUP'''
cols, rows = (10, 15) #n.b. coords are 0-9 by 0-14
wires = [(7,3), (7,6)] #want the wires to be in the centre, should write a fucntion to calculate the points (hanfway down and a third and two thirds across respectively so that it can be scaled up more easily/i dont have to pick points)
box = np.zeros((rows, cols))

box[wires[0][0]][wires[0][1]] = 10
box[wires[1][0]][wires[1][1]] = -10

'''FUNCTIONS'''
def getSurround(col, row):
    up = (col, row-1)
    down = (col, row+1)
    left = (col-1, row)
    right = (col+1, row)

    return up, down, left, right

def getCoordValue(coord, array):
    value = array[coord[0]][coord[1]]

    return value

def getAverage(col, row, array):
    surroundCoords = getSurround(col, row)
    val = 0
    for item in surroundCoords:
        val += getCoordValue(item, array)

    avg = val / len(surroundCoords)

    return avg

def checkNotEdge(coord, box): ##TODO: test me
    if coord[0] == 0 or coord[0] == box.shape[0]:
        return False
    if coord[1] == 0 or coord[1] == box.shape[1]:
        return False

def checkNotWire(coord, wires): ##TODO: test me
    if (coord) != wires[0] and (coord) != wires[1]:
        return False

#make this an 'iterate' function when it works
for row in range(rows):
    for col in range(cols):
        if checkNotWire((col, row), wires): 
            if checkNotEdge((col, row), box):
                avg = getAverage(col, row, box)
                box[col][row] = avg


'''TESTING'''
def testGetSurround():
    #arrange
    box = np.zeros((rows, cols))
    col, row = 3, 2

    #act
    surround = getSurround(col, row)

    #assert
    assert surround[0] == (3, 1)
    assert surround[1] == (3, 3)
    assert surround[2] == (2, 2)
    assert surround[3] == (4, 2)

def testCoordVal():
    #arrange
    testarray = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    #act
    val = getCoordValue((1, 1), testarray)

    #assert
    assert val == 1

def testGetAverage():
    #arrange
    testarray = [0, 2, 0], [3, 0, 5], [0, 2, 0]
    testcol, testrow = 1, 1

    #act
    result = getAverage(testcol, testrow, testarray)


    #assert
    assert result == 3

# testGetSurround()
# testCoordVal()
# testGetAverage()
