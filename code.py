import numpy as np
import statistics as stats

'''SETUP'''
cols, rows = (10, 15) #n.b. coords are 0-9 by 0-14
wires = [(7,3), (7,6)] #want the wires to be in the centre, should write a fucntion to calculate the points (hanfway down and a third and two thirds across respectively so that it can be scaled up more easily/i dont have to pick points)
box = np.zeros((rows, cols)) #grid is 10 columns across by 15 rows down, its just confusing here

box[wires[0][0]][wires[0][1]] = 10
box[wires[1][0]][wires[1][1]] = -10

print(box)

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

    avg = val / 4

    return avg

def checkNotEdge(coord, array):
    if coord[0] == 0 or coord[0] == array.shape[0]-1:
        return False
    elif coord[1] == 0 or coord[1] == array.shape[1]-1:
        return False
    else:
        return True

def checkNotWire(coord, wirelist):
    if (coord) == wirelist[0] or (coord) == wirelist[1]:
        return False
    else:
        return True

#TODO: make this an 'iterate' function when it works
for row in range(rows):
    for col in range(cols):
        if checkNotWire((col, row), wires):
            if checkNotEdge((col, row), box):
                print(col, row)

                # avg = getAverage(col, row, box)
                # box[(col,row)] = avg # updates the original square with the average of its neighbours?


'''TESTING'''
def testGetSurround():
    #arrange
    testarray = np.zeros((rows, cols))
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

def testNotEdgeZero():
    #arrange
    testarray = np.zeros((rows, cols))
    xzero = (0, 10)
    yzero = (8, 0)
    bothzero = (0, 0)

    #act
    xzresult = checkNotEdge(xzero, testarray)
    yzresult = checkNotEdge(yzero, testarray)
    bothresult = checkNotEdge(bothzero, testarray)

    #assert
    assert xzresult == False
    assert yzresult == False
    assert bothresult == False

def testMiddle():
    #arrange
    testarray = np.zeros((rows, cols))
    coord = (5, 7)
    wirelist = (1, 1), (8, 6)

    #act
    edgetest = checkNotEdge(coord, testarray)
    wiretest = checkNotWire(coord, wirelist)

    #assert
    assert edgetest == True
    assert wiretest == True

def testNotEdgeMax():
    #arrange
    testarray = np.zeros((rows, cols))
    xmax = (14, 2)
    ymax = (1, 9)
    bothmax = (14, 9)
    
    #act
    xmresult = checkNotEdge(xmax, testarray)
    ymresult = checkNotEdge(ymax, testarray)
    bothresult = checkNotEdge(bothmax, testarray)

    #assert
    assert xmresult == False
    assert ymresult == False
    assert bothresult == False

def testNotWire():
    #arrange
    testarray = np.zeros((5, 5))
    testwires = (3, 4), (2, 1)

    #act
    result = checkNotWire((3, 4), testwires)
    

    #assert
    assert result == False

testGetSurround()
testCoordVal()
testGetAverage()
testNotEdgeZero()
testNotEdgeMax()
testNotWire()
testMiddle()

