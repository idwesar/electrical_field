import numpy as np
import statistics as stats

'''SETUP'''
rows, cols = (15, 10) #n.b. coords are 0-9 by 0-14
wires = [(7,3), (7,6)] #want the wires to be in the centre, should write a fucntion to calculate the points (hanfway down and a third and two thirds across respectively so that it can be scaled up more easily/i dont have to pick points)
box = np.zeros((rows, cols))

box[wires[0][0]][wires[0][1]] = 10
box[wires[1][0]][wires[1][1]] = -10

'''FUNCTIONS'''
def getSurround(row, col):
    up = (row-1, col)
    down = (row+1, col)
    left = (row, col-1)
    right = (row, col+1)

    return up, down, left, right

def getCoordValue(row, col, array):
    value = array[row][col]

    return value

def getAverage(row, col, array):
    surroundCoords = getSurround(row, col)
    val = 0
    for item in surroundCoords:
        val += getCoordValue(item[0], item[1], array)

    avg = val / 4

    return avg

def checkNotEdge(row, col, array):
    if row == 0 or row == array.shape[0]-1:
        return False
    elif col == 0 or col == array.shape[1]-1:
        return False
    else:
        return True

def checkNotWire(row, col, wirelist):
    if (row, col) == wirelist[0] or (row, col) == wirelist[1]:
        return False
    else:
        return True


#TODO: make this an 'iterate' function when it works
for row in range(rows):
    for col in range(cols):
        if checkNotWire(row, col, wires):
            if checkNotEdge(row, col, box):
                print(row, col)
                avg = getAverage(row, col, box)
                box[(row, col)] = round(avg, 2) # updates the original square with the average of its neighbours?

print(box)


'''TESTING'''
def testGetSurround():
    #arrange
    testarray = np.zeros((rows, cols))
    testrow, testcol = 3, 2

    #act
    surround = getSurround(testrow, testcol)

    #assert
    assert surround[0] == (2, 2)
    assert surround[1] == (4, 2)
    assert surround[2] == (3, 1)
    assert surround[3] == (3, 3)

def testCoordVal():
    #arrange
    testarray = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    #act
    val = getCoordValue(1, 1, testarray)

    #assert
    assert val == 1

def testGetAverage():
    #arrange
    testarray = [0, 2, 0], [3, 0, 5], [0, 2, 0]
    testrow, testcol = 1, 1

    #act
    result = getAverage(testrow, testcol, testarray)


    #assert
    assert result == 3

def testNotEdgeZero():
    #arrange
    testarray = np.zeros((rows, cols))
    xzrow, xzcol = 0, 10
    yzrow, yzcol = 8, 0
    bothzrow, bothzcol = 0, 0

    #act
    xzresult = checkNotEdge(xzrow,xzcol, testarray)
    yzresult = checkNotEdge(yzrow, yzcol, testarray)
    bothresult = checkNotEdge(bothzrow, bothzcol, testarray)

    #assert
    assert xzresult == False
    assert yzresult == False
    assert bothresult == False

def testMiddle():
    #arrange
    testarray = np.zeros((rows, cols))
    row, col = 5, 7
    wirelist = (1, 1), (8, 6)

    #act
    edgetest = checkNotEdge(row, col, testarray)
    wiretest = checkNotWire(row, col, wirelist)

    #assert
    assert edgetest == True
    assert wiretest == True

def testNotEdgeMax():
    #arrange
    testarray = np.zeros((rows, cols))
    xmaxrow, xmaxcol = 14, 2
    ymaxrow, ymaxcol = 1, 9
    bmaxrow, bmaxcol = 14, 9
    
    #act
    xmresult = checkNotEdge(xmaxrow, xmaxcol, testarray)
    ymresult = checkNotEdge(ymaxrow, ymaxcol, testarray)
    bothresult = checkNotEdge(bmaxrow, bmaxcol, testarray)

    #assert
    assert xmresult == False
    assert ymresult == False
    assert bothresult == False

def testNotWire():
    #arrange
    testarray = np.zeros((5, 5))
    testwires = (3, 4), (2, 1)

    #act
    result = checkNotWire(3, 4, testwires)
    

    #assert
    assert result == False

testGetSurround()
testCoordVal()
testGetAverage()
testNotEdgeZero()
testNotEdgeMax()
testNotWire()
testMiddle()

#TODO: put the relevant stuff into a main function pls.
