from pull_data import *
from structs import PlateAppearance as PA

def getInRange(numList, lowerBound, upperBound):
    """
    Returns list of integers in specified range
    PARAMETERS
    -----------
    numList: List of integers to iterate
    lowerBound: INCLUSIVE lower bound of range
    upperBound: INCLUSIVE upper bound of range
    """
    in_range_list = []
    for i in numList:
        try:
            current_num = int(i)
            if lowerBound > upperBound:
                #i.e. 800 to 100
                if current_num >= lowerBound or current_num <= upperBound:
                    in_range_list.append(current_num)
            else:
                if current_num >= lowerBound and current_num <= upperBound:
                    in_range_list.append(current_num)
        except ValueError:
            #if there is non int value, ignore
            pass
    return in_range_list

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