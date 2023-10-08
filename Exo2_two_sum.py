"""
PROGRAM NAME - two_sum
PROGRAMMER - Kuriozity
LANGUAGE - Python 
SYSTEM - Windows 11
DATE - Completed 10/08/2023
NDP - None :)
"""



def two_sum(numbers, target):
    """
    Takes a list of integers and gives the two indices that numbers add up to target.
    
    Args:
        numbers (list of int) : integers to test.
        target (int) : goal to obtain.
    
    Returns:
        indices (list of int): final two indices that gives the target.
    """

    num_indices = {}

    for index,value in enumerate(numbers):
        if target-value in num_indices:
            return [num_indices[target-value], index]
        num_indices[value] = index

    return []


# Test the function
numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))
