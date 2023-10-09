"""
PROGRAM NAME - sum_of_multiply
PROGRAMMER - Mélanie Geulin (melanie.geulin@gmail.com)
LANGUAGE - Python (no add-on libraries)
SYSTEM - Windows 11
DATE - Completed 20/06/2023
BUGS - None :)
"""
def sum_of_multiples(n, limit):
    """
    Returns sum of multiple of n inferior to limit.
    
    Args:
        n (int): The number to multiply.
        limit (int): The number to not surpass.
    
    Returns:
        sum_ (int): Sum of the multiple of n inferior to limit.
    """
    sum_ = 0

    for count in range(n, limit, n):
        sum_ += count
    
    return sum_

# Test the function
n = 3
limit = 10
print(sum_of_multiples(n, limit))
