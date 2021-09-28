import numpy as np
import statistics as stats

'''SETUP'''
cols, rows = (10, 15) #n.b. coords are 0-9 by 0-14
wires = [(7,3), (7,6)] #want the wires to be in the centre, should write a fucntion to calculate the points (hanfway down and a third and two thirds across respectively so that it can be scaled up more easily/i dont have to pick points)
box = np.zeros((rows, cols))

box[wires[0][0]][wires[0][1]] = 10
box[wires[1][0]][wires[1][1]] = 10


#ok now average the four squares around a square

#loop through - the top of the box will be slower but itll all even out eventually

#access a point and get its coords
# for row in range(rows):
#     for col in range(cols):
        # if (col, row) != wires[0] or wires[1]:


        #     print(up)

        #     avg = stats.fmean(positions)

            # box[col][row] = avg



def getSurround(col, row):
    up = (col, row-1)
    down = (col, row+1)
    left = (col-1, row)
    right = (col+1, row)

    return up, down, left, right

def getCoordValue(coord, array):
    value = array[coord[0][coord[1]]]

    return value
    
# def getAverage():
    #get values of up, down, left, and right
    #add them together
    #divide by four
    #return one value

'''TESTING'''
def testGetSurround():
    #arrange
    box = np.zeros((rows, cols))
    col, row = 3, 2

    #act
    surround = getSurround(col, row)

    #assert
    assert len(surround) == 4 #ok but this doesnt really test it, prob make this test better

def testCoordVal():
    #need to a value into an array, preferably 2d, and then access it to see if the function pulls the value when given coordinates



# testGetSurround()
testCoordVal()

