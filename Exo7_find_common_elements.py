"""
PROGRAM NAME - find_common_elements
PROGRAMMER - Mélanie Geulin (melanie.geulin@gmail.com)
LANGUAGE - Python 
SYSTEM - Windows 11
DATE - Completed 21/06/2023
NDP - None :)
"""

def find_common_elements(first_list, second_list):
    """
    Find and list common elements between two lists.
    
    Args:
        first_list (list): list to test.
        second_list (list): list to compare.
    
    Returns:
        result (list): list of common elements.
    """
    result = []
    
    for i in range(len(first_list)):
        if first_list[i] in second_list:
            result.append(first_list[i])
    
    return sorted(result)
        

# Test the function
first_list = [1, 8, 3, 4, 5]
second_list = [4, 5, 6, 7, 8]
print(find_common_elements(first_list, second_list))
