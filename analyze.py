from pull_data import *
from structs import PlateAppearance as PA

def countInRange(numList, lowerBound, upperBound):
    """
    Count the number of ints within two bounds
    PARAMETERS
    -----------
    numList: List of integers to count from
    lowerBound: INCLUSIVE lower bound of range
    upperBound: INCLUSIVE upper bound of range
    """
    count = 0
    for i in numList:
        try:
            current_num = int(i)
            if current_num >= lowerBound and current_num <= upperBound:
                count+= 1
        except ValueError:
            #if there is an auto or no pitch, keep going
            pass
    return count

def getDiff(num1, num2):
    try:
        diff = int(num2) - int(num1)
        if diff <= -500 or diff > 500:
            if num2 > num1:
                return num2 - num1 - 1000
            else:
                return num2 - num1 + 1000
        else:
            return diff
    except ValueError:
        return "x"

def getDiffs(numList):
    '''
    Calculates the difference between numbers in a list (within a range of -499 to 500)
    PARAMETERS
    ----------
    numList: List of numbers to iterate through
    '''
    prev_num = "x"
    diff_list = []
    for i in numList:
        try:
            diff = getDiff(int(i), int(prev_num))
            diff_list.append(diff)
        except ValueError:
            #add 'x' to the list if a diff is not possible to calculate
            diff_list.append("x")
        prev_num = i
    return diff_list


    




data = PlayerData("63", False)
print(getDiffs(data.getPitches()))