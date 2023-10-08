"""
PROGRAM NAME - count_elements
PROGRAMMER - Kuriozity
LANGUAGE - Python + collections
SYSTEM - Windows 11
DATE - Completed 20/06/2023
NDP - One solution use a library, the other not
"""
from collections import Counter

def count_elements(lst):
    """
    Counts how many times there's each element in the list and display dictionnary.
    
    Args:
        lst (list): list of elements to count.
    
    Returns:
        my_dictionnary (dict): dictionnary accounting recurrency of every element.
    """
    """sequence = []
    values = []

    for i in range(1, max(lst)+1):
        sequence.append(i)

    my_dictionnary = dict.fromkeys(sequence, 0)

    for i in range(1, max(lst)+1):
        for j in range(len(lst)):
            if i == lst[j]:
                my_dictionnary[i] += 1 """
    
    my_dictionary = dict(Counter(lst))

    return my_dictionary

# Test the function
lst = [1, 2, 1, 3, 2, 4, 5, 1]
print(count_elements(lst))
